#!/bin/bash

idle python2.7 spaget.py &&
sleep 5 &&
wmctrl -a spaget &&
xdotool key F5
