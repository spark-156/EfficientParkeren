import MySQLdb as mariadb
db = mariadb.connect(host="192.168.178.88", user='RaspberryPiSensoren', passwd='DaanDaan123', db='ParkeergarageA3')
cursor = db.cursor()

db.query("""INSERT INTO `AantalBezet` (`ID`, `Datum`, `Tijd`, `AantalBezet`) VALUES (NULL, CURRENT_DATE(), CURRENT_TIME(), 1);""")