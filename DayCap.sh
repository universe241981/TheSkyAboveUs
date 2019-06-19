#!/bin/bash
while :
do
  DATE=$(date +"%Y%m%d_%H%M%S")
  raspistill -o /home/aspi/AllSkyData/$DATE.jpg &
sleep 60
done
