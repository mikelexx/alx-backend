import { createClient } from 'redis';
const client = createClient();
client.on('connect', ()=>{
 console.log('Redis client connected to the server');
})
client.on('error', (err)=>console.log(`Redis client not connected to the server: ${err}`));
function setNewSchool(schoolName, value){
  client.set(schoolName, value, (err, reply)=>{
    if(err){
      console.log(`Error in setting redis key val: ${err}`);
    }
    else{
      console.log(`Reply: ${reply}`);
    }
  })
}
function displaySchoolValue(schoolName){
  client.get(schoolName,(err, value)=>{
    if (err){
console.log(`displaySchoolValue got error in retrieving key val  using redis clientInstance: ${err}`);
    }
    else{
      console.log(value);
    }
  })
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
