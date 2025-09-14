
class Auto:
    def info(self):
        return "Jsem auto"
class Kolo:
    def info(self):
        return "Jsem kolo"
class Motorka:
    def info(self):
        return "Jsem motorka"
    
def vyber_vozu(typ):
    if typ == "auto":
        return Auto()
    elif typ == "kolo":
        return Kolo()
    elif typ == "motorka":
        return Motorka()
    else:
        return ValueError("Neznamy charakter")
    
typ = input("Zadejte jedno z vozidel (auto, motorka, kolo): ")
obj = vyber_vozu(typ)
print(obj.info())

