import RPi.GPIO as GPIO
import time
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

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

def lampjes():
    dist=distance1()
    if dist > 25:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
    elif dist < 25:
        GPIO.output(green, GPIO.LOW)
        GPIO.output(red, GPIO.HIGH)