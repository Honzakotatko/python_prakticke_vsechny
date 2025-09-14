"""
jmeno = input("Zadejte jmeno: ")
vek = int(input("Zadejte vek: "))

with open("uzivatele.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f"Jmeno: {jmeno}, Vek: {vek}")
    
with open("uzivatele.txt", "r", encoding="utf-8") as read_txt_file:
    cteni = read_txt_file.read()
    
print(cteni)
"""
"""
import csv

studenti = [
    {"jmeno": "Petr", "vek": 18},
    {"jmeno": "Anna", "vek": 19},
    {"jmeno": "Jan", "vek": 17}
]

with open("studenti.csv", "w", newline="", encoding="utf-8") as write_csv_file:
    field = ["jmeno", "vek"]
    
    writer = csv.DictWriter(write_csv_file, fieldnames=field)
    writer.writeheader(field)
    writer.writerows(studenti)

"""
"""
with open("studenti.csv", "r", newline="", encoding="utf-8") as read_csv_file:
    reader = csv.DictReader(read_csv_file)
    for row in reader:
        print(f"{row['jmeno']} - {row['vek']} let")
"""
"""
import json

knihy = {
    "1984": {"autor": "George Orwell", "rok": 1949},
    "Hobit": {"autor": "J. R. R. Tolkien", "rok": 1937}
}

with open("knihy.json", "w", encoding="utf-8") as write_json_file:
    json.dump(knihy, write_json_file)

"""
"""
with open("knihy.json", "r", encoding="utf-8") as read_json_file:
    cteni = json.load(read_json_file)
    
    for klic, info in cteni.items():
        print(f"Nazevc: {klic}, Autor: {info['autor']}, Rok: {info['rok']}")
"""
"""
zamestnanci = {
    "001": {"jmeno": "Petr", "pozice": "Programátor", "plat": 40000},
    "002": {"jmeno": "Anna", "pozice": "Tester", "plat": 35000}
}

zamestnanci["003"] = {"jmeno": "Jan", "pozice": "Analytik", "plat": 42000}

zamestnanci["002"] = {"jmeno": "Anna", "pozice": "Tester", "plat": 37000}

del zamestnanci["001"]

for klic, info in zamestnanci.items():
    print(f"ID: {klic}, Jmeno: {info['jmeno']}, Pozice: {info['pozice']}, Plat: {info['plat']}")
    
if "004" in zamestnanci:
    print(f"{zamestnanci['004']}")
    
else:
    print("Zaměstnanec s ID 004 nebyl nalezen")

"""

"""
produkty = {"rohlík": 3, "mléko": 20, "máslo": 45}

produkty["syr"] = 60

produkty["mléko"] = 22

del produkty["rohlík"]

for klic, hodnota in produkty.items():
    print(f"Produkt: {klic}, Cena: {hodnota} Kc")
    
if "cokolada" in produkty:
    print(f"{produkty['cokolada']}")
    
else:
    print("Cokolada neni v nabidce")
"""
"""
import threading
import time

def soucet(N):
    vysledek = sum(range(1, N + 1))
    print(f"Soucet cisel do {N} je {vysledek}")
    
vlakno1 = threading.Thread(target=soucet, args=(5, ))
vlakno2 = threading.Thread(target=soucet, args=(10, ))
vlakno3 = threading.Thread(target=soucet, args=(20, ))

vlakno1.start()
vlakno2.start()
vlakno3.start()

vlakno1.join()
vlakno2.join()
vlakno3.join()

print("Konec vypoctu!")
"""
"""
class VekChyba(Exception):
    pass

def over_vek(vek):
    if vek >= 18:
        print("Vstup je povolen")
    else:
        raise VekChyba("Musi vam byt minimalne 18 let")
    
try:
    over_vek(18)
except VekChyba as e:
    print(f"Chyba: {e}")
"""
"""
import re

with open("slova.txt", "r", encoding="utf-8") as slova_file:
    slova = slova_file.read()
    
print(slova)

vyskyt_python = re.findall(r"\bPython\b", slova)

print(f"Pocet vyskytu slova Python: {len(vyskyt_python)}")
"""
"""
import csv

with open("produkty.csv", encoding="utf-8") as produkty_file:
    reader = csv.DictReader(produkty_file, delimiter=";")
    seznam = []
    for ovoce in reader:
        ovoce["cena"] = int(ovoce["cena"])
        seznam.append(ovoce["cena"])
        
        soucet = sum(seznam)
print(soucet)
"""
"""
import json

data = [
    {"jmeno": "Adam", "vek": 20},
    {"jmeno": "Petr", "vek": 26},
    {"jmeno": "Franta", "vek": 35},
    {"jmeno": "Karel", "vek": 18}
]

with open("osoba.json", "r", encoding="utf-8") as json_file:
    load = json.load(json_file)
    seznam = []
    for klic in load:
        klic["vek"] = int(klic["vek"])
        seznam.append(klic["vek"])
    pocet = len(seznam)
    soucet = sum(seznam)
    
print(soucet/pocet)
"""
"""
import csv

data = [
    {"jmeno": "Honza", "znamka": 1},
    {"jmeno": "Petr", "znamka": 4},
    {"jmeno": "Karel", "znamka": 2}
]

with open("produkty.csv", encoding="utf-8") as csv_file:
    seznam = []
    reader = csv.DictReader(csv_file)
    
    for klic in reader:
        klic["znamka"] = int(klic["znamka"])
        
        seznam.append(klic["znamka"])
        
        vysledek = sum(seznam)
        
print(vysledek)
"""
"""
import json

data = [
    {"jmeno": "Adam", "vek": 20, "student": True}
]
        
with open("osoba.json", "r", encoding="utf-8") as json_file:
    seznam = []
    reader = json.load(json_file)
    for klic in reader:
        klic["vek"] = int(klic["vek"])
        
        seznam.append(klic["vek"])
        
    pocet = len(seznam)
    soucet = sum(seznam)
    
print(soucet/pocet)
"""


kontakty = {}

kontakty["Adam"] = 704708178
kontakty["Petr"] = 776618123
kontakty["Karel"] = 548217245

def zobraz_kontakty():
    for jmeno, cislo in kontakty.items():
        print(f"Jmeno: {jmeno}, Telefonni cislo: {cislo}")
        
 
def pridej_kontakt():
    jmeno = input("Zadejte jmeno kontaktu: ")
    cislo = input("Zadejte nove cislo: ")
    kontakty[jmeno] = cislo
    print(f"Kontakt byl pridan| Jmeno: {jmeno}, Telefonni cislo: {cislo}")
    
    
def smaz_kontakt():
    jmeno = input("Zadejte jmeno: ")
    if jmeno in kontakty:
        del kontakty[jmeno]
        print("Kontakt byl smazan")
    else:
        print("Kontakt nebyl nalezen")
            
def vyhledej_kontakt():
    jmeno = input("Zadejte jmeno pro vyhledani: ")
    if jmeno in kontakty:
        print(f"Kontakt byl nalezen: {kontakty[jmeno]}")
    else:
        print("Kontakt nebyl nalezen")
    
def upravit_kontakt():
    jmeno = input("Zadejte jmeno pro vyhledani: ")
    if jmeno in kontakty:
        cislo = input("Zadejte nove cislo: ")
        kontakty[jmeno] = cislo
        print(f"Zmena se povedla| Jmeno: {jmeno}, Telefonni cislo: {cislo}")
    else:
        print("Zadane jmeno neexistuje")

while True:
    print("1 pro zobrazeni kontaktu")
    print("2 pro pridani kontaktu")
    print("3 pro smazani kontaktu")
    print("4 pro vyhledani kontaktu")
    print("5 pro upraveni kontaktu")
    print("6 pro konec")
    
    volba = input("Zadejte cislo pro vyber: ")
    
    if volba == "1":
        zobraz_kontakty()
    elif volba == "2":
        pridej_kontakt()
    elif volba == "3":
        smaz_kontakt()
    elif volba == "4":
        vyhledej_kontakt()
    elif volba == "5":
        upravit_kontakt()
    elif volba == "6":
        print("Konec programu")
        break
    else:
        print("Zkuste to znovu")

"""

class NespravneHesloError(Exception):
    pass

spravne_heslo = "Roblox"
pocet_pokusu = 0


while pocet_pokusu <= 3:
    heslo = input("Zadejte heslo: ")
    if heslo == "Roblox":
        print("Heslo je Spravne")
        break
    else:
        pocet_pokusu += 1
        print("Heslo je Spatne zkuste to znovu!")
        if pocet_pokusu == 3:
            raise NespravneHesloError("3x Jste zadal spatne heslo")
"""
"""
def make_node(value, left=None, right=None):
    return {"val": value, "left": left, "right": right}


def insert(tree, value):
    if tree is None:
        return make_node(value)
    if value < tree["val"]:
        tree["left"] = insert(tree["left"], value)
    elif value > tree["val"]:
        tree["right"] = insert(tree["right"], value)
    return tree


def inorder(tree):
    if tree:
        inorder(tree["left"])
        print(tree["val"], end=" ")
        inorder(tree["right"])
        
        
strom = None

for i in [24, 87, 48, 34, 75]:
    strom = insert(strom, i)
    
print("\nInorder:")
inorder(strom)

"""
"""
hovno = input("Zadejte text: ")

def roblox(neco):
    return f"{neco}"


print(roblox(hovno))
"""
"""
slovnik = {
    "stat": {
        "Cesko": "Praha",
        "Nemecko": "Berlin",
        "Slovensko": "Bratislava"
    }
}



slovnik["stat"]["Francie"] = "Pariz"
slovnik["stat"]["Italie"] = "Rim"
slovnik["stat"]["Poslko"] = "Varsava"


def vypis():
    stat = input("Zadejte nazev statu: ")
    if stat in slovnik["stat"]:
        print(slovnik["stat"][stat])
    else:
        print("Tento stat neni ve slovniku")


while True:
    print("Zadejte 1 pro vypsani mesta")
    print("\nZadejte 2 pro ukonceni")

    vstup = input("Zadejte cislo pro vyber: ")
    
    if vstup == "1":
        vypis()
    elif vstup == "2":
        break
    else:
       print("Zadal jste spatne cislo zkuste to znovu!!")
"""
"""
class Uzel:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.vlevo = None
        self.vpravo = None


def vloz(koren, cislo):
    if koren is None:
        return Uzel(cislo)
    if cislo < koren.hodnota:
        koren.vlevo = vloz(koren.vlevo, cislo)
    elif cislo > koren.hodnota:
        koren.vpravo = vloz(koren.vpravo, cislo)
    return koren

def inorder(koren):
    if koren:
        inorder(koren.vlevo)
        print(koren.hodnota, end=" ")
        inorder(koren.vpravo)
    



strom = None
cisla = [15, 24, 87, 68, 12, 47]



"""