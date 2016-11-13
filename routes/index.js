var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', {
    title: 'Express',
    jquery: '/modules/jquery/dist/jquery.min.js',
    frameCapture: 'javascripts/frameCapture.js'
  });
});

module.exports = router;
