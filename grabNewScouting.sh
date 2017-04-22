#!/bin/bash

echo "Pulling Files"
adb devices | awk 'NR>1{print $1}' | xargs -n1 -I% adb -s % pull /sdcard/Download /home/nomythic/RoboticsAppServerSidePythonScripts-master/scouting_files

echo "Removing Files"
#adb shell rm -r /sdcard/Download/*
