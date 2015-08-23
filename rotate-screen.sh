#!/bin/bash
orientation=`xrandr --properties | grep eDP1 | cut -d ' ' -f5 | sed 's/(//g'`

case "$orientation" in
normal)
	xrandr --output "eDP1" --rotate inverted
	xinput disable "PS/2 Generic Mouse"
	xinput set-prop 'SYNAPTICS Synaptics Touch Digitizer V04' 'Evdev Axis Inversion' 180 180
	;;
inverted)
	xrandr --output "eDP1" --rotate normal
	xinput enable "PS/2 Generic Mouse"
	xinput set-prop 'SYNAPTICS Synaptics Touch Digitizer V04' 'Evdev Axis Inversion' 0 0
	;;
esac
