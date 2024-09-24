export default function createPushNotificationsJobs(jobs, queue){
  if(!Array.isArray(jobs)){
  throw new Error('Jobs is not an array');
  }
  jobs.forEach((job)=>{
    const sheduledJob = queue.create('push_notification_code_3', job).save(err=>{
      if(err){
        console.log(`Notification job ${sheduledJob.id} failed: ${err}`);
      }
      else{
        console.log(`Notification job created: ${sheduledJob.id}`);
      }
    });
    sheduledJob.on('complete', ()=>console.log(`Notification job ${sheduledJob.id} completed`));
    sheduledJob.on('failed', (err)=>console.log(`Notification job ${sheduledJob.id} failed: ${err}`));
    sheduledJob.on('progress', (progress, _)=>console.log(`Notification job ${sheduledJob.id} ${progress}% complete`))
  })
}
