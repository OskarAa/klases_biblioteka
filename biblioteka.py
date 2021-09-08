Klases nosaukums
class Robots:
"""Klase reprezentē robotu ar specifisku vārdu."""
# Klases konstruktors. Ar šo metodi tiek inicializēts objekts.
def __init__(self, vards):
"""Datu inicializācija."""
# Īpašības definēšana
self.vards = vards
print("(Inicializējam {})".format(self.vards))
# Metode, kas izvada tekstu
def iznicinat(self):
print("{} tiek iznīcināts!".format(self.vards))
# Metode, kas izvada tekstu
def sasveicinaties(self):
print("Sveiks! Mani sauc {}.".format(self.vards))

2. Klases pārbaude un reāla izmantošana
# 1. robota izveide
droid1 = Robots("R2-D2")
# 1. robota metodes pārbaude
droid1.sasveicinaties()
# 2. robota izveide
droid2 = Robots("C-3PO")
°
# 2. robota metodes pārbaude
droid2.sasveicinaties()

print("\nRoboti šeit var paveikt kādu darbu..\n")
print("Roboti visu ir izdarījuši. Mēs viņus varam iznīcināt.")
droid1.iznicinat()
droid2.iznicinat()

versija = 1
saraksts = ['maize', 'olas', 'piens']
def summa(a, b):
return a + b
class Auto:
def braukt(self):
print("Auto brauc!")

import biblioteka
print(biblioteka.versija)
for prece in biblioteka.saraksts:
print(prece)
print(biblioteka.summa(2, 3))
bmw = biblioteka.Auto()
bmw.braukt()
import biblioteka as bibl
print(bibl.versija)
for prece in bibl.saraksts:
print(prece)
print(bibl.summa(2, 3))
bmw = bibl.Auto()
bmw.braukt()

from biblioteka import *
print(versija)
for prece in saraksts:
print(prece)
print(summa(2, 3))
bmw = Auto()
bmw.braukt()
from biblioteka import versija, summa
print(versija)
# Saraksts nav pievienots, tādēļ cikls nestrādās.
# for prece in saraksts:
# print(prece)
print(summa(2, 3))
# Klase Auto nav pievienota, tādēļ nevar izveidot objektu.
# bmw = Auto()
# bmw.braukt()