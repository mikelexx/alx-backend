import createPushNotificationsJobs from './8-job';
import chai from 'chai';
import sinon from 'sinon';
const kue = require('kue');
const expect = chai.expect;
const queue = kue.createQueue();
describe('createPushNotificationsJobs', function() {
  let createStub; // Declare createStub at the top level
  this.beforeEach(function(){
    queue.testMode.enter();
  })
  this.afterEach(function() {
    queue.testMode.clear();
    queue.testMode.exit();
    if (createStub) {
      createStub.restore(); // Restore the original function
    }
  });
  it('should display an error message if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });
  it('should create two new jobs to the queue', function() {
    const jobs = [
      { code: 223, phone: '+254345' },
      { code: 344, phone: '+456' }
    ];
    createPushNotificationsJobs(jobs, queue);
  });
});
