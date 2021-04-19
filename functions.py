def greet(name):
    greeting = "Welcome {0}!".format(name)
    return greeting


def zusammenzaehlen(sum1, sum2):
    result = sum1 + sum2
    return result


def quadrieren(num1):
    quadriert = num1*num1
    return quadriert


def liste_umsort(liste1):
    list2 = []
    for i in range(len(liste1)-1, -1, -1):
        list2.append(liste1[i])
    return list2


def zeichenketten_umkehren(zeichenkette1, zeichenkette2):
    result = zeichenkette2 + zeichenkette1
    return result


def schrittzaehler(distanz, schrittlaenge):
    result = distanz*100 / schrittlaenge
    return result


def encode(zeichenkette):
    codiert = ""
    for element in range(0, len(zeichenkette)):
        aktuelles_zeichen = zeichenkette[element]
        asci_wert = ord(aktuelles_zeichen)
        asci_wert = asci_wert+1
        codiert = codiert+chr(asci_wert)
    return codiert

def decode(zeichenkette):
    codiert = ""
    for element in range(0, len(zeichenkette)):
        aktuelles_zeichen = zeichenkette[element]
        asci_wert = ord(aktuelles_zeichen)
        asci_wert = asci_wert-1
        codiert = codiert+chr(asci_wert)
    return codiert
