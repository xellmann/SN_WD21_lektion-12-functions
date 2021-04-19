from functions import *

name = input("Enter your name: ")
greeting1 = greet(name)
print(greeting1)
print(greet(name))

print(zusammenzaehlen(15, 2))

print(quadrieren(5))

x = [1, 5, 3, 9]

print(liste_umsort(liste1=x))

print(zeichenketten_umkehren("zeichen", "kette"))

distanz = float(input("Wie weit bist du gegangen[m]: "))
schrittlaenge = float(input("Wie groß ist deine Schrittlänge[cm]: "))

print("Du bist " + str(schrittzaehler(distanz=distanz, schrittlaenge=schrittlaenge)) + " Schritte gegangen")

zeichenkette = input("Insert text to encode: ")
codierte_zeichenkette = encode(zeichenkette)
print(codierte_zeichenkette)

print(decode(codierte_zeichenkette))
