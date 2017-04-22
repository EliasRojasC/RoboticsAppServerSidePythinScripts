# !/bin/bash


for line in `adb devices | grep -v "List"  | awk '{print $1}'`
do
  device=`echo $line | awk '{print $1}'`
  echo "$device $@ ..."
  adb -s $device $@ adb shell ls /sdcard 
done
