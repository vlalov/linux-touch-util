#!/usr/bin/python
#
# Source of the theory: https://wiki.archlinux.org/index.php/Calibrating_Touchscreen
#

import subprocess;
import re;

def findTouch():
  xinput_output = subprocess.check_output(['xinput']);


def setTouch(c0, c2, c1, c3):
  result = subprocess.call(['xinput', 'set-prop', 'SYNAPTICS Synaptics Touch Digitizer V04', 
			    '--type=float', 'Coordinate Transformation Matrix', 
			    str(c0), '0', str(c1), '0', str(c2), str(c3), '0', '0', '1']);
  if result > 0:
    print("xinput returned with code " + str(result));

def main():
  xrandr_output = subprocess.check_output(['xrandr']);
  pattern = re.compile('(e?DP\\d|HDMI\\d) connected (?:primary )?(\\d+)x(\\d+)\\+(\\d+)\\+(\\d+)');
  matchers = pattern.finditer(xrandr_output);
  
  total_width = 0;
  total_height = 0;
  touch_height = 0;
  touch_width = 0;
  touch_offset_x = 0;
  touch_offset_y = 0;
  
  for match in matchers:
    if match.group(1) == 'eDP1':
      touch_width = int(match.group(2));
      touch_height = int(match.group(3));
      touch_offset_x = int(match.group(4));
      touch_offset_y = int(match.group(5));
    total_width = max(total_width, int(match.group(2)) + int(match.group(4)));
    total_height = max(total_height, int(match.group(3)) + int(match.group(5)));

  setTouch(float(touch_width)/total_width, float(touch_height)/total_height, 
	   float(touch_offset_x)/total_width, float(touch_offset_y)/total_height);

if __name__ == '__main__':
  main()
