var fs = require('fs'),
  path = require('path'),
  Twit = require('twit'),
  spawn = require('child_process').spawn,
  config = require(path.join(__dirname, 'config.js'));;

function getLogTimestamp() {
  return new Date().toISOString().replace(/T/, ' ').replace(/\..+/, '')
}

console.log(getLogTimestamp() + ' - Generating new passage.');

dummy = spawn('python3', [path.join(__dirname, 'bible_markov.py')])

dummy.stdout.on('data', function(data) {
  var passage = data.toString()

  console.log(getLogTimestamp() + ' - Logging new passage: ' + passage);

  T.post('statuses/update', {
    status: passage
  }, function(err, data, response) {
    if (err) {
      console.log('Error when tweeting!');
      console.log(err)
    } else {
      console.log(getLogTimestamp() + ' - Successfully tweeted.');
    }
  });

});


var T = new Twit(config);
