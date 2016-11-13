var express = require('express');
var spawn = require("child_process")
var multer = require('multer');
var jimp = require('jimp');
var fs = require('fs');

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
var emotion = '-1';

router.get('/', function(req, res, next) {
  res.render('index', { title: 'This is the API' });
});

router.route("/upload").post(upload.single('avatar'), function(req, res, next) {
  console.log(req.file);
  jimp.read('uploads/test.png', function (err, image) {
    image.resize(48, 48).greyscale().write('uploads/test.png');
    spawn.exec('python python/main.py', function(err, stdout, stderr) {
      if (err) {
        console.log("child processes failed with error code: " + err.code);
      }
      console.log(stdout);
      fs.readFile('result.txt', 'utf8', function(err, data) {
        if (err) {
          console.log(err);
        }
        emotion = data;
        res.end(data);
      })
    });
  });
});

router.get('/emotion', function(req, res, next) {
  res.end(emotion)
});

module.exports = router;
