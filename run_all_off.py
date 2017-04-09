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
	rtc.alloff()
except KeyboardInterrupt:
	rtc.terminate()
