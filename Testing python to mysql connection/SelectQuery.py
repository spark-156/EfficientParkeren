import MySQLdb as mariadb
db = mariadb.connect(host="192.168.178.88", user='RaspberryPiSensoren', passwd='DaanDaan123', db='ParkeergarageA3')
cursor = db.cursor()

# "SELECT ID, Datum, Tijd, AantalBezet FROM AantalBezet"

db.query("""SELECT ID, Datum, Tijd, AantalBezet FROM AantalBezet""")
r = db.store_result()
print(r.fetch_row(5))
