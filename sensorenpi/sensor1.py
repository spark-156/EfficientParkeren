import RPi.GPIO as GPIO
import time

#Mode GPIO pinnen
GPIO.setmode(GPIO.BCM)

#GPIO pinnen aanwijzen
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


def afstand1():
    # Zet de trigger aan.
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.001)
    #Zet de trigger uit na 1 ms.
    GPIO.output(GPIO_TRIGGER, False)

    StartTijd = time.time()
    StopTijd = time.time()

    # opslaan startTijd.
    while GPIO.input(GPIO_ECHO) == 0:
        StartTijd = time.time()

    # Opslaan signaal aankomst
    while GPIO.input(GPIO_ECHO) == 1:
        StopTijd = time.time()

    # Verschil in tijd tussen versturen en ontvangen.
    TijdVerlopen = StopTijd - StartTijd
    # Vermenigvuldig met de geluidssnelheid. (34300 cm/s)
    # Deel de afstand door 2, want het signaal gaat heen en weer.
    Afstand1 = (TijdVerlopen * 34300) / 2

    return Afstand1

def lampjes():
    dist=distance1()
    if dist > 25:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
    elif dist < 25:
        GPIO.output(green, GPIO.LOW)
        GPIO.output(red, GPIO.HIGH)