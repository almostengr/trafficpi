#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_flash_green.py
# Created: 	2017-05-07
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Flashes all of green signals
################################################################################

import raspitraffic as rtc
from time import sleep

try:
        rtc.setup()
        phasenum=7

        while True:
                phasenum=rtc.controlflasher(phasenum)
                sleep(rtc.getflashsleep())

except KeyboardInterrupt:
        rtc.terminate()

