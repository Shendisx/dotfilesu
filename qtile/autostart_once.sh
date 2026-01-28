#!/bin/bash

# Apply wallpaper using wal
wal -b 282738 -i ~/Wallpaper/Aesthetic2.png &&

# Start picom
picom --config ~/.config/picom/picom.conf &

/usr/bin/lxqt-policykit-agent &
/usr/bin/dunst &
/usr/bin/jamesdsp &
xset r rate 220 60 &
xset s off &
xrandr --output HDMI-A-0 --set TearFree on &
