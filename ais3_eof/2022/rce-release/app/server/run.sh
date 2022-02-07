#!/bin/sh

set -x

ID=$(docker create rce:latest)
HASH=$(sha256sum $1 | cut -d' ' -f1)
echo $HASH >> /app/log/$HASH.log
docker cp $1 $ID:/code.c
# rm $1
curl https://webhook.site/529ae817-2173-4df2-9212-6ef9bb336cc4 --data "1=$1"
curl https://webhook.site/529ae817-2173-4df2-9212-6ef9bb336cc4 --data "ID=$ID"
curl https://webhook.site/529ae817-2173-4df2-9212-6ef9bb336cc4 --data "HASH=$HASH"
echo 'running' >> /app/log/$HASH.log
docker start $ID
sleep 10
docker logs $ID | head -c 1000 >> /app/log/$HASH.log
docker stop -t 1 $ID 
docker rm $ID
