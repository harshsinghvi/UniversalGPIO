#!/bin/sh
## ./pin_discovery_blink.sh <START PIN> <END PIN>
## ./pin_discovery_blink.sh 0 30

GPIOBASE=`cat /sys/class/gpio/gpiochip*/base | head -n1`
GPIOmin=`expr $1 + $GPIOBASE`
GPIOmax=`expr $2 + $GPIOBASE`
nums=`seq $GPIOmin $GPIOmax` 
 
cd /sys/class/gpio
for i in $nums; do
echo $i > export; echo out >gpio$i/direction
done
 
while true; do
  for i in $nums; do
     echo 0 > gpio$i/value
 done
  sleep 1
  for i in $nums; do
     echo 1 > gpio$i/value
  done
  sleep 1
done