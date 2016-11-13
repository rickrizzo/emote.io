var express = require('express');
var router = express.Router();
fs = require('fs');
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {
    title: 'Express',
    jquery: '/modules/jquery/dist/jquery.min.js',
    frameCapture: 'javascripts/frameCapture.js'
  });
});



router.get('/data', function(req, res, next) {
  fs.readFile('result.txt', 'utf8', function(err, data) {
    if (err) {
      console.log(err);
    }
    emotion = data;
    res.send(data);
  })
	// res.send('hello world')
});

module.exports = router;
