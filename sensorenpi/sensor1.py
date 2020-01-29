import RPi.GPIO as GPIO
import time

#Mode GPIO pinnen
GPIO.setmode(GPIO.BCM)

#GPIO pinnen aanwijzen
GPIO_TRIGGER = 18
GPIO_ECHO = 24

blauw = 17
groen = 27
rood = 22

#Instellingen GPIO pinnen bij opstarten.
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(rood, GPIO.OUT)
GPIO.output(rood, GPIO.LOW)
GPIO.setup(groen, GPIO.OUT)
GPIO.output(groen, GPIO.LOW)
GPIO.setup(blauw, GPIO.OUT)
GPIO.output(blauw, GPIO.LOW)


def afstand1():
    ''''Berekent de afstand tussen de sensor en het dichtstbijzijnde voorwerp.'''
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
    ''''Lampje gaat rood branden als de afstand tot het dichtstbijzijnde voorwerp kleiner dan 25centimeter is en
     groen branden als de afstand groter dan 25 centimeter is.'''
    Afstandsensor1=afstand1()
    if Afstandsensor1 > 25:
        GPIO.output(rood, GPIO.LOW)
        GPIO.output(groen, GPIO.HIGH)
    elif Afstandsensor1 < 25:
        GPIO.output(groen, GPIO.LOW)
        GPIO.output(rood, GPIO.HIGH)