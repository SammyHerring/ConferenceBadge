#!/usr/bin/env python

import math
import time
import scrollphat
import sys

def millis():
    return int(round(time.time() * 1000))

scrollphat.set_brightness(2)
scrollphat.write_string("Sammy Herring  |||  SportTrax  |||  sherring.me  |||  ") #Leave x number of blank spaces to prevent overlap

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
