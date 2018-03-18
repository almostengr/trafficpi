#!/usr/bin/python

################################################################################
# Project: 	Raspi Traffic Control
# Script Usage: run_all_on.py
# Created: 	2017-04-09
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Turns on all the lights and exits.
################################################################################

# import raspitraffic as rtc
import trafficcontrol as rtc

try:
	rtc.setup()
except KeyboardInterrupt:
	rtc.terminate()

