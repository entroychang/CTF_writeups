#!/bin/sh

apk add nodejs npm curl

cd /app && npm install

while [ ! -f /certs/client/cert.pem ]
do
  sleep 5
done
sleep 30 # nasty way to wait for dind start
docker build -t rce:latest /app

mkdir /app/log
node app.js
