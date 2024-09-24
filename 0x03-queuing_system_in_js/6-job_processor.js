import {kue} from 'kue';
const queue = kue.createQueue();
queue.on('error', (err)=>{
  console.log(`error connecting with redis server: ${err}`);
});
function sendNotification(phoneNumber, message){
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
};
queue.process('push_notification_code', (job, done)=>{
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
