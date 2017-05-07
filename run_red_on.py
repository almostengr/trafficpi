#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_red_on.py
# Created: 	2017-05-07
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Turns on the red light on all signals.
################################################################################

import raspitraffic as rtc

try:
	rtc.setup()
	rtc.nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
	rtc.eblight(LMPON, LMPOFF, LMPOFF)
except KeyboardInterrupt:
	rtc.terminate()
