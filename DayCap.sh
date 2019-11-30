#!/bin/bash
while :
do
  DATE=$(date --utc +"%Y%m%d-%H%M%S%Z")
  raspistill -o /home/aspi/AllSkyData/$DATE.jpg -mm spot -br 45 &
sleep 60
done

#For 8MP Pi camera v2
#raspistill -mm backlit -drc high -o $DATE.jpg -w 1640 -h 1232 &

# DATE=$(date --utc +"%Y%m%d_%H%M%S%Z")
