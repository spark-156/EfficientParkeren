import sensor1 as s1
import sensor2 as s2
import time
import RPi.GPIO as GPIO
import MySQLdb as mariadb
import MySqlConnection as sql

db = mariadb.connect(host="server.local", user='RaspberryPiSensoren', passwd='DaanDaan123', db='ParkeergarageA3')
cursor = db.cursor()

#Mode GPIO pinnen
GPIO.setmode(GPIO.BCM)

bezet1, bezet2 = 0, 0
switch1, switch2 = 1, 1

#GPIO pinnen aanwijzen
groenDrukte = 5
blauwDrukte = 6
roodDrukte = 11

#Instellingen GPIO pinnen bij opstarten.
GPIO.setup(roodDrukte, GPIO.OUT)
GPIO.output(roodDrukte, GPIO.LOW)
GPIO.setup(blauwDrukte, GPIO.OUT)
GPIO.output(blauwDrukte, GPIO.LOW)
GPIO.setup(groenDrukte, GPIO.OUT)
GPIO.output(groenDrukte, GPIO.LOW)


def drukte():
    ''''Lampje gaat groen branden als alle plekken vrij zijn, blauw branden als 1 van de 2 plekken bezet is
    en het lampje gaat rood branden als beide plekken bezet zijn.'''
    if dist1 > 25 and dist2 > 25:
        #Lampje brand groen.
        GPIO.output(blauwDrukte, GPIO.LOW)
        GPIO.output(roodDrukte, GPIO.LOW)
        GPIO.output(groenDrukte, GPIO.HIGH)
    elif dist1 < 25 and dist2 < 25:
        #Lampje brand rood.
        GPIO.output(blauwDrukte, GPIO.LOW)
        GPIO.output(groenDrukte, GPIO.LOW)
        GPIO.output(roodDrukte, GPIO.HIGH)
    elif dist1 > 25 and dist2 < 25 or dist2 > 25 and dist1 < 25:
        #Lampje brand blauw.
        GPIO.output(roodDrukte, GPIO.LOW)
        GPIO.output(groenDrukte, GPIO.LOW)
        GPIO.output(blauwDrukte, GPIO.HIGH)


try:
    while True:
        AfstandSensor1 = s1.afstand1()
        print("sensor 1 = %.1f cm" % AfstandSensor1)
        if bezet1 == 1 and switch1 == 1:
            # raakt1 bezet
            sql.Aantalbezet(db, True)
            sql.Parkeerplek(db, 1, 1)
            switch1 = 0
        elif bezet1 == 0 and switch1 == 0:
            # raakt vrij
            sql.Aantalbezet(db, False)
            sql.Parkeerplek(db, 1, 0)
            switch1 = 1
        elif AfstandSensor1 < 25:
            bezet1 = 1
        elif AfstandSensor1 > 25:
            bezet1 = 0
        s1.lampjes()
        AfstandSensor2 = s2.afstand2()
        print("sensor 2 = %.1f cm" % dist2)
        if bezet2 == 1 and switch2 == 1:
            sql.Aantalbezet(db, True)
            sql.Parkeerplek(db, 2, 1)
            switch2 = 0
        elif bezet2 == 0 and switch2 == 0:
            sql.Aantalbezet(db, False)
            sql.Parkeerplek(db, 2, 0)
            switch2 = 1
        elif AfstandSensor2 < 25:
            bezet2 = 1
        elif AfstandSensor2 > 25:
            bezet2 = 0
        s2.lampjes()
        drukte()
        time.sleep(4)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Measurement stopped by User")
    