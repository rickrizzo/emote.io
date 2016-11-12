var express = require('express');
var path = require('path');
var formidable = require('formidable');
var fs = require('fs');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'This is the API' });
});

router.post('/upload', function(req, res, next) {
  var form = new formidable.IncomingForm();
  form.multiples = false;
  form.uploadDir = '/uploads';

  form.on('file', function(fields, file) {
    fs.rename(file.path, path.join(form.uploadDir, file.name));
  });

  form.on('error', function(err) {
    console.log("ERROR: " + err);
  });

  form.on('end', function() {
    res.end('success');
  });

  form.parse(req);
});

module.exports = router;
