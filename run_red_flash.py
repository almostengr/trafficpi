#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_flash_red.py
# Created: 	2017-05-07
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Flashes all of the red lights on the signals.
################################################################################

import raspitraffic as rtc
from time import sleep

try:
	rtc.setup()
	phasenum=3
	
	while True:
		phasenum=rtc.controlflasher(phasenum)
                sleep(rtc.getflashsleep())

except KeyboardInterrupt:
        rtc.terminate()

