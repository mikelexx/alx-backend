import { createClient } from 'redis';
const client = createClient();
client.on('connect', ()=>{
 console.log('Redis client connected to the server');
})
client.on('error', (err)=>console.log(`Redis client not connected to the server: ${err}`));
client.connect();
function setNewSchool(schoolName, value){
  if(client.isOpen){
    client.set(schoolName, value).then(msg=>{
      console.log(`Reply: ${msg}`);
    }).catch(err=>console.log(`Error in setting redis key val: ${err}`));
  }
}
function displaySchoolValue(schoolName){
  if(client.isOpen){
    client.get(schoolName).then(msg=>{
      console.log(msg);
    }).catch(err=>console.log(`displaySchoolValue got error in retrieving key val  using clientInstance: ${err}`));
  }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
