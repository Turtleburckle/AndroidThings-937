import RPI.GPIO as GPIO
import os

buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

while True:
    if GPIO.input(buttonPin):
        os.system("python/home/pi/sendNotify.py")