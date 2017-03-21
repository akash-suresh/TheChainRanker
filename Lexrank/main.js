var lexrank = require('lexrank');
var originalText = 'some...text...here...';
var topLines = lexrank.summarize(originalText, 5, function (err, toplines, text) {
  if (err) {
    console.log(err);
  }
  console.log(toplines);
  console.log(originalText);