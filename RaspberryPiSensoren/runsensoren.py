import sensor1 as s1
import sensor2 as s2
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

green = 5
red = 6

GPIO.setup(red, GPIO.OUT)
GPIO.output(red, GPIO.LOW)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.LOW)

try:
    while True:
        dist = s1.distance1()
        print("Measured distance = %.1f cm" % dist)
        s1.lampjes()
        time.sleep(2)

        dist2 = s2.distance2()
        print("Gemeten afstand = %.1f cm" % dist2)
        s2.lampjes()
        time.sleep(2)

        if dist > 20 and dist2 > 20:
            GPIO.output(red, GPIO.LOW)
            GPIO.output(green, GPIO.HIGH)
        if dist < 20 and dist2 < 20:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()