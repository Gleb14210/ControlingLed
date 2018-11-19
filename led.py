#file = open("testfile.txt", "w")

#file.write( "gpio=%d=%s,%s" % (17, "op", "dh") )
#file.truncate(0)

#file.close()

import RPi.GPIO as GPIO
#import os
import time
#import subprocess
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while True:
	GPIO.output(12, 0)
	time.sleep(0.3)
	GPIO.output(12, 1)
	time.sleep(0.3)

GPIO.cleanup()
