const kue = require('kue');
const queue = kue.createQueue();
const data = {
  phoneNumber: '+2541234567',
  message: '55898234',
}
const job = queue.create('push_notification_code', data).save((err)=>{
  if(err){
    console.log('Notification job failed');
  }
  else{
    console.log(`Notification job created: ${job.id} ID`);
  }
});
job.on('complete', ()=>console.log('Notification job completed'));
