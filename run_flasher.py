#!/usr/bin/python

################################################################################
# Project:      Traffic Control
# Script Usage: run_flasher.py
# Created:      2017-04-02
# Author:       Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:  Flash lights as if a malfunction or power outage has occurred.
################################################################################

import raspitraffic as rtc
from time import sleep

try:
	rtc.setup()
	phaseflasher=1

	while True:
		phaseflasher=rtc.controlflasher(phaseflasher)
		sleep(rtc.getflashsleep())
except KeyboardInterrupt:
	rtc.terminate()
