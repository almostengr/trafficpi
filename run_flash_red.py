#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_all_off.py
# Created: 	2017-04-09
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Turns off all of the lights and exits.
################################################################################

import raspitraffic as rtc

try:
	rtc.setup()
	
	while True:
		rtc.nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		rtc.eblight(LMPON, LMPOFF, LMPOFF)

		sleep(.5)

		rtc.nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		rtc.eblight(LMPOFF, LMPOFF, LMPOFF)

		sleep(.5)

except KeyboardInterrupt:
	rtc.terminate()
