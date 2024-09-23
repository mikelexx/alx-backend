import redis from 'redis';
const client = redis.createClient();
client.on('connect', ()=>{
 console.log('Redis client connected to the server');
})
client.on('error', (err)=>console.log(`Redis client not connected to the server: ${err}`));
const cities = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];
for(let idx = 0; idx < cities.length; idx++){
  client.hset('HolbertonSchools', cities[idx], values[idx], redis.print);
}
client.hgetall('HolbertonSchools', (err, reply)=>{
  if(err){
    console.log(`Error in hgetall: ${err}`);
  }
  else{
console.log(reply);
  }
})
