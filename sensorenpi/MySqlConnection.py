import MySQLdb as mariadb

def Aantalbezet(db, optie):
    """Haalt aantal huidige bezette plekken op uit de database en telt er een bij op of af. Hierna wordt de nieuwe waarde weer naar de database gestuurd."""
    db.query('''SELECT AantalBezet FROM AantalBezet ORDER BY ID DESC LIMIT 1''')
    result = db.store_result()
    aantalbezet = result.fetch_row(1)[0][0]
    if optie == True:
        aantalbezet += 1
    elif optie == False:
        aantalbezet -= 1
    db.query("""INSERT INTO `AantalBezet` (`ID`, `Datum`, `Tijd`, `AantalBezet`) VALUES (NULL, CURRENT_DATE(), CURRENT_TIME(), '{}');""".format(aantalbezet))
    db.commit()
    print('aantalbezet committed', aantalbezet)
    return None

def Parkeerplek(db, Parkeerplek, Bezet):
    """Zet in de database wanneer een parkeerplek aangegeven met parkeerplek bezet wordt of vrij raakt."""
    db.query('''INSERT INTO `Parkeerplek{}` (`ID`, `Datum`, `Tijd`, `Bezet`) VALUES (NULL, CURRENT_DATE(), CURRENT_TIME(), '{}');'''.format(Parkeerplek, Bezet))
    db.commit()
    print('parkeerplek committed', Parkeerplek, Bezet)
    return None