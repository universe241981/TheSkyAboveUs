#!/bin/bash
while :
do
  DATE=$(date +"%Y%m%d_%H%M%S")
  raspistill -ISO 800 -ss 6500000 -o /home/aspi/AllSkyData/$DATE.jpg -q 100 &
sleep 60
done
