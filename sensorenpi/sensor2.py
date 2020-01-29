import RPi.GPIO as GPIO
import time

#Mode GPIO pinnen
GPIO.setmode(GPIO.BCM)

#GPIO pinnen aanwijzen.
GPIO_TRIGGER2 = 20
GPIO_ECHO2 = 21

blauw2 = 26
green2 = 19
red2 = 13

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(red2, GPIO.OUT)
GPIO.output(red2, GPIO.LOW)
GPIO.setup(green2, GPIO.OUT)
GPIO.output(green2, GPIO.LOW)
GPIO.setup(blue2, GPIO.OUT)
GPIO.output(blue2, GPIO.LOW)


def afstand2():
    # Zet de trigger aan.
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.001)
    # Zet de trigger uit na 1 ms.
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
    Afstand2 = (TijdVerlopen * 34300) / 2

    return Afstand2

def lampjes():
    ''''Lampje gaat rood of groen branden aan de hand van de afstand tot het dichtstbijzijnde voorwerp.'''
    AfstandSensor2=afstand2()
    if AfstandSensor2 > 25:
        GPIO.output(red2, GPIO.LOW)
        GPIO.output(green2, GPIO.HIGH)
    elif AfstandSensor2 < 25:
        GPIO.output(green2, GPIO.LOW)
        GPIO.output(red2, GPIO.HIGH)
