import RPi.GPIO as GPIO
import time

#Mode GPIO pinnen
GPIO.setmode(GPIO.BCM)

#GPIO pinnen aanwijzen.
GPIO_TRIGGER2 = 20
GPIO_ECHO2 = 21

blauw2 = 26
groen2 = 19
rood2 = 13

#Instellingen GPIO pinnen bij opstarten.
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(rood2, GPIO.OUT)
GPIO.output(rood2, GPIO.LOW)
GPIO.setup(groen2, GPIO.OUT)
GPIO.output(groen2, GPIO.LOW)
GPIO.setup(blauw2, GPIO.OUT)
GPIO.output(blauw2, GPIO.LOW)


def afstand2():
    ''''Berekent de afstand tussen de sensor en het dichtstbijzijnde voorwerp.'''
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
    ''''Lampje gaat rood branden als de afstand tot het dichtstbijzijnde voorwerp kleiner dan 25centimeter is en
     groen branden als de afstand groter dan 25 centimeter is.'''
    AfstandSensor2=afstand2()
    if AfstandSensor2 > 25:
        GPIO.output(rood2, GPIO.LOW)
        GPIO.output(groen2, GPIO.HIGH)
    elif AfstandSensor2 < 25:
        GPIO.output(groen2, GPIO.LOW)
        GPIO.output(rood2, GPIO.HIGH)
