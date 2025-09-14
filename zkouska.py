"""
list = [82, 59, 105, 75, 21]
list.sort()
print(list)
"""
"""
text = input("Zadej text:")
print(len(text))
"""
"""
a = int(input("Zadejte prvni cislo:"))
b = int(input("Zadejte druhe cislo:"))

def soucet(a,b):
    return a + b
def soucin(a,b):
    return a * b
def rozdil(a,b):
    return a - b
def podil(a,b):
    return a / b

print(soucet(a,b))
print(soucin(a,b))
print(rozdil(a,b))
print(podil(a,b))
"""
"""
text1 = input("Zadejte text jedna:")
text2 = input("Zadejte text dva:")
text3 = input("Zadejte text tri:")
text4 = input("Zadejte text ctyri:")

text = "." .join([text1, text2, text3, text4])
print(text)
"""
"""
for _ in range(0, 3):
    cislo = int(input("zadejte cislo:"))

    if 20 > cislo :
        print("cislo je mensi nez 20")
    elif 20 <= cislo <= 30:
        print("cislo je mezi 20 a 30")
    else:
        print("cislo je vetsi nez 30")
"""
"""
def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cislo = int(input("Zadejte cislo:"))
for i in range(cislo):
    print(fibonacci(i))
"""
"""
jmeno = input("Jmeno:")
vek = int(input("Vek:"))

vystup = print(f"Ahoj jmenuji se {jmeno} a je mi {vek} let. \nDnes je velmi krasny den")
"""
"""
class Animals:
    def __init__ (self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def makeSound(self):
        return "Nejaky zvireci zvuk"
    
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        
    def makeSound(self):
        return "Woof Woof"
    
dog1 = Dog("Rex", 8, 46)
dog2 = Dog("Buddy", 5, 52)

print("jmeno psa:", dog2.name)
print("vek psa:", dog2.age)
print("vyska psa:", dog2.height)
print("zvuk psa:", dog2.makeSound())

"""






"""
list = [59, 84, 20, 78]
list.sort()
print(list)
"""
"""
text = input("text:")
print(len(text))
"""
"""
a = int(input("cislo 1"))
b = int(input("cislo 2"))

def soucet(a,b):
    return a + b
def soucin(a,b):
    return a * b
def podil(a,b):
    return a / b
def rozdil(a,b):
    return a - b

print(soucet(a,b))
print(soucin(a,b))
print(podil(a,b))
print(rozdil(a,b))
"""
"""
t1 = input("t1:")
t2 = input("t2:")
t3 = input("t3:")
t4 = input("t4:")

vysledek = "." .join([t1, t2, t3, t4])
print(vysledek)
"""
"""
for x in range(0,3):
    cislo = int(input("Zadejte cislo:"))
    
    if cislo < 20:
        print("cislo je mensi nez 20")
    elif 20 <= cislo <= 30:
        print("cislo je mezi 20 a 30")
    else:
        print("cislo je vetsi nez 30")
"""
"""
def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cisla = int(input("Cisla:"))
for i in range(cisla):
    print(fibonacci(i))
"""
"""
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def makeSound(self):
        return "Nejaky psi zvuk"
    
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    def makeSound(self):
        return "Woof Woof"
    
dog1 = Dog("Rex", 5, 40)
dog2 = Dog("Buddy", 8, 52)

print(dog1.name, dog1.age, dog1.height)
print(dog1.makeSound())
"""
"""
jmeno = input("jmeno:")
vek = int(input("vek"))

vystup = print(f"Ahoj jmenuji se {jmeno} a je mi {vek} let \nDnes je velmi krasny den")
"""
"""
from datetime import datetime

cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print(cas)
    
"""
"""
vek = int(input("vek:"))

vystup = "Dospely" if vek >= 18 else "nezletily"
print(vystup)
"""
"""

def hello(name):
    print(f"Hello, {name}")
    
hello("Petr")
"""
"""
retezec = "Python"
print(retezec[0])
print(retezec[-1])

"""





"""
cisla = input("cisla oddelene mezerou:")
cisla = list(map(int, cisla.split()))
cisla.sort()
print(cisla)
"""
"""

text = input("text:")
print(len(text))
"""
"""
a = int(input("Zadejte cislo 1:"))
b = int(input("Zadejte cislo 2:"))

def soucet(a,b):
    return a + b
def soucin(a,b):
    return a * b
def rozdil(a,b):
    return a - b
def podil(a,b):
    return a / b

print(soucet(a,b))
print(soucin(a,b))
print(podil(a,b))
print(rozdil(a,b))
"""
"""
text1 = input("text1:")
text2 = input("text2:")
text3 = input("text3:")
text4 = input("text4:")

vysledek = ".".join([text1, text2, text3, text4])
print(vysledek)
"""
"""
for i in range(0,3):
    cislo = int(input("Zadejte cislo:"))
    if cislo < 20:
        print("cislo je mensi nez 20")
    elif 20 <= cislo <= 30:
        print("Cislo je mezi 20 a 30")
    else:
        print("cislo je vetsi nez 30")
"""
"""   
def fibonacci(x):
    if x <= 0:
        return 0
    elif x== 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
cisla = int(input("Zadejte pocet posloupnosti:"))
for i in range(cisla):
    print(fibonacci(i))
"""
"""
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def makeSound(self):
        return "Nejaky psi zvuk"
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
            
    def makeSound(self):
        return "Woof Woof"
    
dog1 = Dog("Rex", 10, 42)

print(dog1.name, dog1.age, dog1.height)
print(dog1.makeSound())

"""
"""
jmeno = input("zadejte jmeno:")
vek = int(input("zadejte vek:"))

print(f"Jmenuji se {jmeno} a je mi {vek} let.\nDnes je velmi krasny den")
"""
"""
from datetime import datetime

cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print(cas)
"""
"""
class Phones:
    def __init__(self, znacka, model, cena):
        self.znacka = znacka
        self.model = model
        self.cena = cena
    def __str__(self):
        return f"{self.znacka} {self.model} - {self.cena} Kc"
    
class PhonesFactory:
    @staticmethod
    def create_phone(znacka, model, cena):
        return Phones(znacka, model, cena)
        
telefon1 = PhonesFactory.create_phone("Apple", "Iphone 15", 25000)

print(telefon1)
"""
"""
cisla = input("cisla:")

cisla = list(map(int, cisla.split()))
cisla.sort()

print(cisla)
"""
"""
def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cislo = int(input("Zadejte pocet cisel:"))

for i in range(cislo):
    print(fibonacci(i))
"""
"""
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def makeSound(self):
        return "nejaky psi zvuk"
    
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        
    def makeSound(self):
        return "Woof Woof"
    
dog = Dog("Rex", 12, 52)

print(dog.name)
print(dog.makeSound())
"""
"""
cisla = input("cisla:")

cisla = list(map(int, cisla.split()))
cisla.sort()
print(cisla)
"""
"""
def fibonacci(x):
    if x<=0:
        return 0
    elif x==1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cisla = int(input("Cisla:"))
for i in range(cisla):
    print(fibonacci(i))
"""
"""
from datetime import datetime

cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print(cas)
"""
"""
class Phones:
    def __init__(self, znacka, cena):
        self.znacka = znacka
        self.cena = cena
    def __str__(self):
        return f"{self.znacka}, {self.cena} Kc"
    
class PhonesFactory:
    @staticmethod
    def create_phone(znacka, cena):
        return Phones(znacka, cena)
    
telefon = PhonesFactory.create_phone("Apple", 25000)

print(telefon)
"""
"""
class Phones:
    def __init__(self, znacka, cena):
        self.znacka = znacka
        self.cena = cena
    def __str__(self):
        return f"{self.znacka}, {self.cena} Kc"
    
class PhonesFactory:
    @staticmethod
    def create_phone(znacka, cena):
        return Phones(znacka, cena)
        
telefon = PhonesFactory.create_phone("Apple", 25000)

print(telefon)
"""
"""
text1 = input("text:")
text2 = input("text:")
text3 = input("text:")
text4 = input("text:")

retezec = ".".join([text1, text2, text3, text4])
print(retezec)
"""

"""
for i in range(0,3):
    cislo = int(input("Zadejte cislo:"))
    if cislo < 20:
        print("cislo je mensi nez 20")
    elif 20 <= cislo <= 30:
        print("Cislo je mezi 20 a 30")
    else:
        print("cislo je vetsi nez 30")
"""
"""
zvirata = ["zajic", "prase", "kun", "pes"]
print(zvirata[0])
print(zvirata[3])

zvirata.append("kocka")
print(zvirata)

zvirata.remove("zajic")
print(zvirata)
        
zvirata.insert(1, "velbloud")
print(zvirata)

zvirata.sort()
"""
"""
cisla = (input("Zadejte cisla:"))

cisla = list(map(int, cisla.split()))
cisla.sort()

print(cisla)
"""
"""
with open("neco.txt", "w", encoding="utf-8") as file:
    for i in range(5):
        text = input(f"Zadej text:")
        file.write(text + "\n")
"""

"""
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def makeSound(self):
        return "Nejaky zvuk psa"
        
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        
    def makeSound(self):
        return "Woof Woof"
        
dog1 = Dog("Rex", 5, 57)

print(dog1.name)

print(dog1.makeSound())
"""
"""
a = int(input("prvni cislo:"))
b = int(input("druhe cislo:"))

def soucin(a, b):
    return a * b
def soucet(a, b):
    return a + b
def rozdil(a, b):
    return a - b
def podil(a, b):
    return a / b

print(soucet(a, b))
print(soucin(a, b))
print(podil(a, b))
print(rozdil(a, b))
"""
"""
def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cisla = int(input("Zadejte pocet posloupnosti:"))
for i in range(cisla):
    print(fibonacci(i))
"""
"""
cisla = [3, 7, 1, 9, 5]
neco = sum(cisla)

print(neco)
"""
"""
class Film:
    def __init__(self, nazev, rok, zanr):
        self.nazev = nazev
        self.rok = rok
        self.zanr = zanr
        
    def __str__(self):
        return f"{self.nazev}, {self.rok}, {self.zanr}"
    
filmy = {}

filmy[0] = Film("Avengers", 2018, "Sci-Fi")
filmy[1] = Film("Avengers", 2018, "Sci-Fi")
filmy[2] = Film("Avengers", 2018, "Sci-Fi")
filmy[3] = Film("Avengers", 2018, "Sci-Fi")
filmy[4] = Film("Hobbit", 2010, "Fantasy")

for id, film in filmy.items():
    print(f"ID: {id} -> {film}")
"""
"""
cisla = input("Zadejte cisla:")
cisla = list(map(int, cisla.split()))   
cisla.sort()

print(cisla)
"""
"""
a = int(input("Zadejte prvni cislo:"))
b = int(input("Zadejte druhe cislo:"))

def soucet(a, b):
    return a + b
def soucin(a, b):
    return a * b
def rozdil(a, b):
    return a - b
def podil(a, b):
    return a / b 

print(soucet(a, b))
print(soucin(a, b))
print(rozdil(a, b))
print(podil(a, b))
"""
"""
text1 = input("Zadejte text:")
text2 = input("Zadejte text:")
text3 = input("Zadejte text:")
text4 = input("Zadejte text:")

vysledek = ".".join([text1, text2, text3, text4])

print(vysledek)
"""
"""
for i in range(3):
    cislo = int(input("Zadejte cislo:"))
    
    if cislo < 20:
        print("Cislo je mensi nez 20")
    elif 20 < cislo < 30:
        print("Cislo je mezi 20 a 30")
    else:
        print("Cislo je vetsi nez 30")
"""
"""
def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

cisla = int(input("Zadejte pocet posloupnosti:"))
for i in range(cisla):
    print(fibonacci(i))
"""
"""
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def makeSound(self):
        return "Nejaky zvuk psa"
    
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        
    def makeSound(self):
        return "Woof Woof"
        
dog1 = Dog("Rex", 8, 52)

print(dog1.age)

print(dog1.makeSound())
"""
"""
jmeno = input("Zadejte sve jmeno:")        
vek = int(input("Zadejte svuj vek:"))

print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.\ndnes je velmi krasny den")
"""
"""
from datetime import datetime

cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

print(cas)
"""
"""
class Phones:
    def __init__(self, znacka, cena):
        self.znacka = znacka
        self.cena = cena
        
    def __str__(self):
        return f"{self.znacka}, {self.cena} Kc"
    
class PhoneFactory:
    @staticmethod
    def create_phone(znacka, cena):
        return Phones(znacka, cena)
    
Phone1 = PhoneFactory.create_phone("Apple", 14999)
Phone2 = PhoneFactory.create_phone("Samsung", 9999)

print(Phone1)
print(Phone2)
"""
"""
class Films:
    def __init__(self, nazev, rok, zanr):
        self.nazev = nazev
        self.rok = rok
        self.zanr = zanr
        
    def __str__(self):
        return f"{self. nazev}, {self.rok}, {self.zanr}"
    
filmy = {}

filmy[0] = Films("Avengers", 2018, "Sci-Fi")
filmy[1] = Films("Avengers", 2018, "Sci-Fi")
filmy[2] = Films("Avengers", 2018, "Sci-Fi")
filmy[3] = Films("Avengers", 2018, "Sci-Fi")
filmy[4] = Films("Roblox", 2011, "Fantasy")

for id, film in filmy.items():
    print(f"ID: {id} -> {film}")
"""
"""
class Filmy:
    def __init__(self, nazev, rok, zanr):
        self.nazev = nazev
        self.rok = rok
        self.zanr = zanr
        
    def __str__(self):
        return f"{self.nazev}, {self.rok}, {self.zanr}"
    
films = {}

films [0] = Filmy("Harry Potter", 2017, "Fantasy")
films [1] = Filmy("Roblox", 2015, "Scifi")
films [2] = Filmy("Fortnite", 2005, "Romantic")

for id, film in films.items():
    print(f"{id} -> {film}")
"""
"""
hash_table = {}

def simple_hash(value):
    return len(value) % 10

def insert(value):
    key = simple_hash(value)
    if key not in hash_table:
        hash_table[key] = []
    hash_table[key].append(value)
    
insert("kocka")
insert("pes")
insert("krecek")
print(hash_table)
"""
"""
class NespravneHesloError(Exception):
    pass

spravne_heslo = "tajne123"

pokusy = 3

for i in range(pokusy):
    zadane_heslo = input("Zadej heslo:")
    if zadane_heslo == spravne_heslo:
        print("Prihlaseni bylo uspesne")
        break
    else:
        ("Spatne heslo")
        
else:
    raise NespravneHesloError("Trikrat spatne napsane heslo pristup odepren")
"""
"""
import threading
import time

def secti_cisla(n):
    time.sleep(1)
    soucet = sum(range(1, n + 1))
    print(f"soucet cisel od 1 do {n} je {soucet}")
    
vlakno = 
"""
"""
cisla = input("Zadejte cisla:")

cisla = list(map(int, cisla.split()))

cisla.sort()

print(cisla)
"""
"""
text = input("Zadejte text:")

print(len(text))
"""
"""
a = int(input("Zadejte prvni cislo:"))
b = int(input("Zadejte druhe cislo:"))

def soucet(a ,b):
    return a + b

def rozdil(a ,b):
    return a - b

def soucin(a ,b):
    return a * b

def podil(a ,b):
    return a / b
        
print(soucet(a,b))
print(rozdil(a,b))
print(soucin(a,b))
print(podil(a,b))
"""
"""
text1 = input("prvni text:")
text2 = input("druhy text:")
text3 = input("treti text:")
text4 = input("ctvrty text:")

vysledek = "." .join([text1, text2, text3, text4])

print(vysledek)
"""
"""
for i in range(0,3):
    cislo = int(input("Zadejte cislo:"))

    if cislo < 20:
        print("cislo je mensi nez 20")
        
    elif 20 < cislo < 30:
        print("cislo je mezi 20 a 30")
        
    else:
        print("cislo je vetsi nez 30")
"""
"""
def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
cisla = int(input("Zadejte pocet cisel posloupnosti:"))
for i in range(cisla):
    print(fibonacci(i))
"""
"""
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def makeSound(self):
        return f"Nejaky zvuk psa"
    
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        
    def makeSound(self):
        return f"Woof Woof"
        
dog1 = Dog("Rex", 12, 59)
dog2 = Dog("Roman", 8, 45)

print(dog2.name)
print(dog2.makeSound())
"""
"""
jmeno = input("Zadej jmeno:")
vek = int(input("Zadej svuj vek"))

print(f"Ahoj jmenuji se {jmeno} a je mi {vek} let. \n Dnes je velmi krasny den")    
"""
"""
from datetime import datetime

cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

print(cas)
"""
"""
class Film:
    def __init__(self, nazev, rok, zanr):
        self.nazev = nazev
        self.rok = rok
        self.zanr = zanr
        
    def __str__(self):
        return f"{self.nazev}, {self.rok}, {self.zanr}"
    
filmy = {}

filmy[0] = Film("Roblox", 2154, "sfasd")
filmy[1] = Film("dasda", 8547, "fasgw")
filmy[2] = Film("Roghsdfvblox", 248, "sfasggxcawd")

for id, film in filmy.items():
    print(f"ID {id} -> {film}")
"""
"""
import re

jmeno = input("Zadejte text: ")

vysledek = r"\b[A-Z][ěščřžýáíéa-z]+\b"

jmenicko = re.search(vysledek, jmeno)

print(jmenicko)
"""
"""
hash = input("Zadejte text: ")

dict = {}

def pridani():
    sum = 0
    for hovna in hash:
        x = ord(hovna)
        sum += x
    return sum

def prevedeni(dict, slovo):
    cislo = pridani()
    dict[cislo] = slovo
    print(dict)
    
prevedeni(dict, hash)
"""






























    


            


