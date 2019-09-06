#!/bin/bash
while :
do
  DATE=$(date +"%Y%m%d_%H%M%S")
  raspistill -o /home/aspi/AllSkyData/$DATE.jpg &
sleep 60
done

#For 8MP Pi camera v2
#raspistill -mm backlit -drc high -o $DATE.jpg -w 1640 -h 1232 &
