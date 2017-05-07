#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_yellow_on.py
# Created: 	2017-05-07
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Turns on the yellow light on all signals.
################################################################################

import raspitraffic as rtc

try:
	rtc.setup()
	rtc.nblight(LMPOFF, LMPON, LMPOFF, LMPON, LMPOFF)
	rtc.eblight(LMPOFF, LMPON, LMPOFF)
except KeyboardInterrupt:
	rtc.terminate()
