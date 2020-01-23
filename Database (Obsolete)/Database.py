import sqlite3
sqlite3.connect('tijden.db')

import sqlite3

conn = sqlite3.connect('tijden.db')
c = conn.cursor()

c.execute('''CREATE TABLE BeginTijd
             ([ID] INTEGER PRIMARY KEY,[Parkeervak] integer, [Datum] date, [Tijd] time)''')

c.execute('''CREATE TABLE EindTijd
             ([ID] INTEGER PRIMARY KEY,[Parkeervak] integer, [Datum] date, [Tijd] time)''')

conn.commit()

