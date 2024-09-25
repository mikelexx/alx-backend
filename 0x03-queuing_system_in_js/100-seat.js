import {util} from 'chai';
import { createClient } from 'redis';
import {promisify} from 'util';
const express = require('express');
const client = createClient();
const hgetAsync = promisify(client.get).bind(client);
const kue = require('kue');
function reserveSeat(number){
  client.set('available_seats', number);
}
async function getCurrentAvailableSeats(){
  try{
    return hgetAsync('available_seats');
  }
  catch(err){
    console.log(err);
  }
}
let reservationEnabled = true;
const queue = kue.createQueue();
const app = express();
app.listen(1245, ()=>reserveSeat(50));
app.get('/available_seats', async (_, res)=>{
    const availableSeats =  await getCurrentAvailableSeats();
    res.json({"numberOfAvailableSeats":availableSeats}).end();
})
app.get('/reserve_seat', (_, res)=>{
  if(!reservationEnabled){
    res.json({ "status": "Reservation are blocked" }).end();
  }
  else {
    const job = queue.create('reserve_seat', {'seatdata': 'data'}).save(err=>{
      if(err){
        res.json({"status": "Reservation failed" }).end();
      }
      else{
        res.json({ "status": "Reservation in process" }).end();
      }
    });
    job.on('complete', ()=>console.log(`Seat reservation job ${job.id} completed`));
    job.on('failed', (err)=>console.log(`Seat reservation job ${job.id} failed: ${err}`));
  }
});
app.get('/process', async (_, res)=>{
  let reservedSeats = await getCurrentAvailableSeats();
  queue.process('reserve_seat', (_, done)=>{
    reserveSeat(reservedSeats - 1);
    reservedSeats = reservedSeats - 1;
    if(reservedSeats == 0){
      reservationEnabled = false;
      done();
    }else if(reservedSeats > 0){
      done();
    }
    else{
      done(new Error('Not enough seats available'));
    }
  });
  res.json({ "status": "Queue processing" }).end();
})
