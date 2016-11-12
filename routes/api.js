var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'This is the API' });
});

router.post('/upload', function(req, res, next) {
  console.log(req.file);
});

module.exports = router;
