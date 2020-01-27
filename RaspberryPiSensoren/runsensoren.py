import sensor1 as s1
import sensor2 as s2
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

greendrukte = 5
bluedrukte = 6
reddrukte = 11

GPIO.setup(reddrukte, GPIO.OUT)
GPIO.output(reddrukte, GPIO.LOW)
GPIO.setup(bluedrukte, GPIO.OUT)
GPIO.output(bluedrukte, GPIO.LOW)
GPIO.setup(greendrukte, GPIO.OUT)
GPIO.output(greendrukte, GPIO.LOW)

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

        if dist > 25 and dist2 > 25:
            GPIO.output(bluedrukte, GPIO.LOW)
            GPIO.output(reddrukte, GPIO.LOW)
            GPIO.output(greendrukte, GPIO.HIGH)
        elif dist < 25 and dist2 < 25:
            GPIO.output(bluedrukte, GPIO.LOW)
            GPIO.output(greendrukte, GPIO.LOW)
            GPIO.output(reddrukte, GPIO.HIGH)
        elif dist > 25 and dist2 < 25 or dist2 > 25 and dist < 25:
            GPIO.output(reddrukte, GPIO.LOW)
            GPIO.output(greendrukte, GPIO.LOW)
            GPIO.output(bluedrukte, GPIO.HIGH)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()