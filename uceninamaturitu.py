"""
try:
    vstup1 = int(input("Zadejte cislo 1: "))
except:
    print("Nespravny vstup zadejte cislo a ne pismeno ci slovo")
    exit()
finally:
    print("Konec prvniho bloku try")
    
try:
    vstup2 = int(input("Zadejte cislo 2: "))
except:
    print("Nespravny vstup zadejte cislo a ne pismeno ci slovo")
    exit()

print("Soucet cisel: " + str(vstup1 + vstup2))
"""
"""
x = 10

while x > 0:
    print("Nazdar")
    x -= 2
    
print("program skoncil")
"""
"""
cislo1 = int(input("Zadejte prvni cislo: "))
cislo2 = int(input("Zadejte druhe cislo: "))
operace = input("Zadejte operaci +, -, *, /: ")


if operace == "+" :
    print(cislo1 + cislo2)
elif operace == "-" :
    print(cislo1 - cislo2)
elif operace == "*" :
    print(cislo1 * cislo2)
elif operace == "/" :
    print(cislo1 / cislo2)
"""
"""
cislo = int(input("Zadejte cislo: "))

zbytek = cislo % 2

if zbytek == 0:
    print("cislo je sude")
else:
    print("cislo je liche")
"""
"""
vaha = float(input("Zadejte svoji vahu v Kg: "))
vyska = float(input("Zadejte svoji vysku v M: "))

bmi = vaha / vyska ** 2

if bmi <= 18.5:
    print("Mate podvahu" + bmi)
elif 18.6 <= bmi <= 24.9:
    print("Mate normalni vahu " + str(bmi))
else:
    print("Mate nadvahu nebo obezitu " + str(bmi)) 
    
"""
"""
cislo1 = int(input("Zadej prvni cislo: "))
cislo2 = int(input("Zadej druhe cislo: "))

if cislo1 == cislo2:
    print("Cisla jsou stejna")
elif cislo1 > cislo2:
    print("Prvni cislo je vetsi nez druhe")
else:
    print("Druhe cislo je vetsi nez prvni")
"""
"""
cislo = int(input("Zadejte cislo ktere chcete nasobit: "))
    
for nasobilka in range(0, 11):
    
    nasobilka += 1 
    
    print(cislo * nasobilka)
"""
"""
cislo = int(input("Zadejte cislo ktere do ktereho chcete provest soucet: "))

soucet = 0
i = 1

while  i <= cislo:
    soucet += i
    i += 1
    
print("Soucet cisel od 1 do", cislo , "je:", soucet) 
"""
"""
x = 10

while x > 0:
    print(x)
    x -= 1
"""
"""
cislo = int(input("Zadejte cislo: "))

for i in range(cislo):
    print(i + 1)
"""
"""
cislo = int(input("Zadejte cislo: "))

for i in range(cislo):
    i += 1
    if i % 2 == 0:
        print(i)
"""
"""
cislo = int(input("Zadejte cislo ktere do ktereho chcete provest soucet: "))

soucet = 0
i = 1

while  i <= cislo:
    soucet = soucet + i
    i = i + 1
    
print("Soucet cisel od 1 do", cislo , "je:", soucet) 
"""

"""
cislo = int(input("Zadejte cislo: "))

for i in range(1, 11):
    print(cislo * i)
"""
"""
cislo = int(input("Zadejte cislo: "))

soucet = 0

for i in range(1, cislo + 1):
    
  if i % 2 == 0:
      soucet += i
      
print(soucet)
"""
"""
pole = 0
pocet_vstupu = 5

for i in range(pocet_vstupu):
    
    vstup = int(input(f"Zadejte {pocet_vstupu} cisel: "))
    pole += vstup
    
print(pole / pocet_vstupu)
"""
"""
cisla = []
uzivatel = int(input("Zadejte pocet cisel:"))

for i in range(uzivatel):
    vstup = int(input("Zadejte cisla:"))
    cisla.append(vstup)

cisla.sort()

print(cisla[-1])
"""
"""
cislo = int(input("Zadejte cislo: "))

if cislo < 0:
    print("Cislo je zaporne")
elif cislo == 0:
    print("Cislo je nula")
else:
    print("Cislo je kladne")
"""
"""
rok = int(input("Zadejte rok: "))

#delitel = rok / 4

if (rok % 4 == 0) or (rok % 400 == 0 and rok % 100 != 0):
    print("Rok je prestupny")
else:
    print("Rok neni prestupny")
"""
"""
cislo1 = int(input("Zadejte prvni cislo: "))
cislo2 = int(input("Zadejte druhe cislo: "))

if cislo1 > cislo2:
    print("Prvni cislo je vetsi nez druhe")
else:
    print("Druhe cislo je vetsi nez prvni")
"""
"""
cisla = int(input("Zadejte cislo: "))

for i in range(cisla):
    i += 1
    print(i)
"""
"""
cisla = int(input("Zadejte cislo: "))

for i in range(cisla):
    i += 1
    if i % 2 == 0:
        print(i)
"""
"""
n = int(input("Zadejte cislo: "))

faktorial = 1


for i in range(1, n + 1):
    
    faktorial = faktorial * i
    
    
print(faktorial)
"""
"""
cislo = int(input("Zadejte cislo: "))

for i in range():
    
"""
"""
from datetime import datetime

now = datetime.now()

cas = datetime.strftime(now, "%d.%m.%Y %H:%M:%S")

print(cas)
"""
"""
from datetime import datetime, timedelta


datum = input("Zadejte datum ve formatu DD.MM.RRRR: ")
prevod = datetime.strptime(datum, "%d.%m.%Y")
now = datetime.now()



rozdil = now - prevod

print(rozdil.days)

"""
"""
class NespravneHesloError(Exception):
    def __init__(self, zprava):
        super().__init__(zprava)

message = "3x jste zadali spatne heslo"
try:
    for i in range(3):
        heslo = input("Zadejte heslo: ")
        if heslo != "Roblox":
            print("Heslo je spatne zkuste to znovu")
            
        else:
            print("Heslo je spravne")
            break

except NespravneHesloError as message:
    print(f"{message}")

"""

knihy = {
    "1984": {"autor": "George Orwell", "rok": 1949},
    "Hobit": {"autor": "J. R. R. Tolkien", "rok": 1937},
    "Kytice": {"autor": "K. J. Erben", "rok": 1853}
}


knihy["Maly princ"] = {"autor": "Antoine de Saint-Exupéry", "rok": 1943}

knihy["Hobit"] = {"autor": "J. R. R. Tolkien", "rok": 1951}

del knihy["1984"]


for nazev, info in knihy.items():
    print(f"Nazev: {nazev}, Autor: {info['autor']}, Rok: {info['rok']}")
    
if "Kytice" in knihy:
    print(f"Autor Kytice : {knihy['Kytice']['autor']}")
    
else:
    print("Kytice tam neni")

"""
class NeplatnyVekError(Exception):
    pass

class NeplatneJmenoError(Exception):
    pass


vek = int(input("Zadejte vek: "))

if vek >= 18:
    jmeno = input("Zadejte jmeno: ")
else:
    raise NeplatnyVekError("Musite byt starsi 18ti let")

if len(jmeno) >= 3:
    print(f"Registrace probehla uspesne! Uzivatel: {jmeno}, Vek: {vek}")
    
else:
    raise NeplatneJmenoError("Musite mit delsi jmeno nez 2 znaky")
"""