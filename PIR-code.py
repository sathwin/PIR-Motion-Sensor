import RPi.GPIO as GPIO
import time
motionPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionPin, GPIO.IN)
time.sleep(10)
try:
    while True:
        motion = GPIO.input(motionPin)
        print(motion)
        time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
