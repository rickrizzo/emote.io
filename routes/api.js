var express = require('express');
var spawn = require("child_process").spawn;
var multer = require('multer');
var jimp = require('jimp');

var options = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, 'uploads')
  },
  filename: function(req, file, cb) {
    cb(null, "test.png")
  }
})

var upload = multer({ storage: options });
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('index', { title: 'This is the API' });
});

router.route("/upload").post(upload.single('avatar'), function(req, res, next) {
  console.log(req.file);
  jimp.read('uploads/test.png', function (err, image) {
    image.resize(48, 48).greyscale().write('uploads/test.png');
  });
  spawn('python',['python/test.py']).stdout.on('data', function(data) {
    res.end(data);
  });
});

module.exports = router;
