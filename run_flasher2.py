#!/usr/bin/python

################################################################################
# Project:      Traffic Control
# Script Usage: run_flasher2.py
# Created:      2017-05-23
# Author:       Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:  Flash lights as if a malfunction or power outage has occurred. 
# 		This script flashes the lights the opposite color of 
#		run_flasher1.py. EB yellow and NB red.
################################################################################

import raspitraffic as rtc

try:
	rtc.setup()
	phaseflasher=9

	while True:
		phaseflasher=rtc.controlflasher(phaseflasher)
		rtc.flashsleep()
except KeyboardInterrupt:
	rtc.terminate()
