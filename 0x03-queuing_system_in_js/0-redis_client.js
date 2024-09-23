import { createClient } from 'redis';
const client = createClient();
// client.connect()
//  .then((_)=>console.log('Redis client connected to the server'))
//  .catch((err)=>console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
