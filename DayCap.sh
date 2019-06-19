#!/bin/bash
while :
do
  DATE=$(date +"%Y%m%d_%H%M%S")
  raspistill -o /home/stargazer/AstroPhoto\ Plus/Sequences/Photos/$DATE.jpg &
sleep 60
done
