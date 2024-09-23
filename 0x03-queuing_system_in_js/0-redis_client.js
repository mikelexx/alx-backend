import { createClient } from 'redis';
async function createRedisClient () {
  try {
    const client = createClient();
    client.on('err', err => console.log(`Redis client not connected to the server: ${err}`));
    client.on('connect', () => console.log('Redis client connected to the server'));
    await client.connect();
  } catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}
createRedisClient();
