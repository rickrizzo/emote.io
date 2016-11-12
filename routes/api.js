var express = require('express');
var multer = require('multer');
var upload = multer({ dest:"upload" });
var spawn = require("child_process").spawn;

var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'This is the API' });
});

router.route("/upload").post(upload.single('avatar'), function(req, res, next) {
  spawn('python',['test.py']).stdout.on('data', function(data) {
    res.end(data);
  });
});

module.exports = router;
