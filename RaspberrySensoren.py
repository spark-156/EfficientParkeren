import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_TRIGGER2 = 20
GPIO_ECHO2 = 21

blue2 = 26
green2 = 19
red2 = 13

blue = 17
green = 27
red = 22

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, GPIO.LOW)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.LOW)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, GPIO.LOW)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(red2, GPIO.OUT)
GPIO.output(red2, GPIO.LOW)
GPIO.setup(green2, GPIO.OUT)
GPIO.output(green2, GPIO.LOW)
GPIO.setup(blue2, GPIO.OUT)
GPIO.output(blue2, GPIO.LOW)


def distance1():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.001)
    GPIO.output(GPIO_TRIGGER, False)

    # set Trigger after 0.01ms to LOW
    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed * 34300) / 2

    return distance1


def distance2():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)

    time.sleep(0.001)
    GPIO.output(GPIO_TRIGGER2, False)

    # set Trigger after 0.01ms to LOW
    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance2 = (TimeElapsed * 34300) / 2

    return distance2


try:
    while True:
        dist = distance1()
        print("Measured Distance = %.1f cm" % dist)
        if dist > 25:
            GPIO.output(blue, GPIO.LOW)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(green, GPIO.HIGH)
        elif dist < 20:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(blue, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
        elif dist > 20 and dist < 25:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        time.sleep(2)

        dist2 = distance2()
        print("Gemeten afstand = %.1f cm" % dist2)
        if dist2 > 25:
            GPIO.output(blue2, GPIO.LOW)
            GPIO.output(red2, GPIO.LOW)
            GPIO.output(green2, GPIO.HIGH)
        elif dist2 < 20:
            GPIO.output(green2, GPIO.LOW)
            GPIO.output(blue2, GPIO.LOW)
            GPIO.output(red2, GPIO.HIGH)
        elif dist2 > 20 and dist2 < 25:
            GPIO.output(green2, GPIO.LOW)
            GPIO.output(red2, GPIO.LOW)
            GPIO.output(blue2, GPIO.HIGH)
        time.sleep(2)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
