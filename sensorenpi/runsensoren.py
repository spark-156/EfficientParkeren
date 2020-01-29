import sensor1 as s1
import sensor2 as s2
import time
import RPi.GPIO as GPIO
import MySQLdb as mariadb
import MySqlConnection as sql

db = mariadb.connect(host="server.local", user='RaspberryPiSensoren', passwd='DaanDaan123', db='ParkeergarageA3')
cursor = db.cursor()

GPIO.setmode(GPIO.BCM)

bezet1, bezet2 = 0, 0
switch1, switch2 = 1, 1

greendrukte = 5
bluedrukte = 6
reddrukte = 11

GPIO.setup(reddrukte, GPIO.OUT)
GPIO.output(reddrukte, GPIO.LOW)
GPIO.setup(bluedrukte, GPIO.OUT)
GPIO.output(bluedrukte, GPIO.LOW)
GPIO.setup(greendrukte, GPIO.OUT)
GPIO.output(greendrukte, GPIO.LOW)


def drukte():
    if dist1 > 25 and dist2 > 25:
        GPIO.output(bluedrukte, GPIO.LOW)
        GPIO.output(reddrukte, GPIO.LOW)
        GPIO.output(greendrukte, GPIO.HIGH)
    elif dist1 < 25 and dist2 < 25:
        GPIO.output(bluedrukte, GPIO.LOW)
        GPIO.output(greendrukte, GPIO.LOW)
        GPIO.output(reddrukte, GPIO.HIGH)
    elif dist1 > 25 and dist2 < 25 or dist2 > 25 and dist1 < 25:
        GPIO.output(reddrukte, GPIO.LOW)
        GPIO.output(greendrukte, GPIO.LOW)
        GPIO.output(bluedrukte, GPIO.HIGH)


try:
    while True:
        switched = 0
        dist1 = s1.distance1()
        print("sensor 1 = %.1f cm" % dist1)
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
        elif dist1 < 25:
            bezet1 = 1
        elif dist1 > 25:
            bezet1 = 0
        s1.lampjes()
        dist2 = s2.distance2()
        print("sensor 2 = %.1f cm" % dist2)
        if bezet2 == 1 and switch2 == 1:
            sql.Aantalbezet(db, True)
            sql.Parkeerplek(db, 2, 1)
            switch2 = 0
        elif bezet2 == 0 and switch2 == 0:
            sql.Aantalbezet(db, False)
            sql.Parkeerplek(db, 2, 0)
            switch2 = 1
        elif dist2 < 25:
            bezet2 = 1
        elif dist2 > 25:
            bezet2 = 0
        s2.lampjes()
        drukte()
        time.sleep(4)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Measurement stopped by User")
    