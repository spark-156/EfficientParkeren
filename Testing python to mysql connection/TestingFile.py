import mariadb as mariadb

connection = mariadb.connect(user="RaspberryPiSensoren", host="server.local", database="ParkeergarageA3", password="DaanDaan123")
print(connection)