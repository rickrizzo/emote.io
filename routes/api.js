var express = require('express');
// var spawn = require("child_process").spawn;
var multer = require('multer');
var upload = multer({ dest:"uploads/" });

var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'This is the API' });
});

router.route('/upload').post(upload.single('avatar'), function(req, res, next) {
  console.log(req.file);
  // spawn('python',['python/test.py']).stdout.on('data', function(data) {
  //   res.end(data);
  // });
  res.end("DONE");
});

module.exports = router;
