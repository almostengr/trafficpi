#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_green_on.py
# Created: 	2017-05-07
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Turns on the green light on all signals.
################################################################################

import raspitraffic as rtc

try:
	rtc.setup()
	rtc.nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPON)
	rtc.eblight(LMPOFF, LMPOFF, LMPON)
except KeyboardInterrupt:
	rtc.terminate()
