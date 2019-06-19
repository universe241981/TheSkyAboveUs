#!/bin/bash
while :
do
  DATE=$(date +"%Y%m%d_%H%M%S")
  raspistill -ISO 800 -ss 8000000 -o /home/stargazer/AstroPhoto\ Plus/Sequences/Photos/$DATE.jpg -q 100 &
sleep 60
done
