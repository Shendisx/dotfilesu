#!/bin/bash

/usr/bin/lxqt-policykit-agent &
/usr/bin/dunst &
/usr/bin/jamesdsp &
xset r rate 220 60 &
xset s off &
xrandr --output HDMI-A-0 --set TearFree on &

