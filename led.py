import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
f = 10

while True:
        GPIO.output(12, 0)
        time.sleep(1/f)
        GPIO.output(12, 1)
        time.sleep(1/f)

GPIO.cleanup()

