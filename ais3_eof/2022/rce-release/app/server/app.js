const express = require('express');
const multer  = require('multer');
const { exec } = require('child_process');
const sha256File = require('sha256-file');

const app = express();
const upload = multer({ dest: '/tmp/' });

app.get('/', function (req, res) {
  res.sendFile('/app/index.html');
});

app.post('/', upload.single('file'), function (req, res) {
  if (typeof req.file === 'undefined') {
    res.status(400).send("file not provided");
    return;
  }
  exec(`docker-entrypoint.sh /app/run.sh ${req.file.path}`);
  res.send(`/log/${sha256File(req.file.path)}.log\n${req.file.path}\n`);
});

app.use('/log', express.static('/app/log'));

app.listen(7414);
