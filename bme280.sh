#!/bin/bash
while :
do
  date -u +"%Y%m%d-%H%M%S%Z" >> bme280.txt
  python bme280.py >> bme280.txt
sleep 60
done
