#!/bin/bash

echo "Pulling Files"
adb shell ls /sdcard/Download/*.csv | tr '\r' ' ' | xargs -n1 adb pull

mv ./*.csv scouting_files

echo "Removing Files"
adb shell rm -r /sdcard/Download/*
