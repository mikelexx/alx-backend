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
function redisClientGetValFromKeyPromise(key){
  return new Promise((resolve, reject)=>{
    client.get(key, (err, val)=>{
      if(err){
        reject(err);
      }else{
        resolve(val);
      }
    })
  });
}
async function displaySchoolValue(schoolName){
  try{
    const val = await redisClientGetValFromKeyPromise(schoolName);
    console.log(val);
  }
  catch(err){
    console.log(`displaySchoolValue got error in retrieving key val  using clientInstance: ${err}`);
  }
}
async function main(){
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}
main();
