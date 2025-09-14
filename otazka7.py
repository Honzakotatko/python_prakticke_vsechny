# Rodičovská třída Animals
class Animals:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def makeSound(self):
        return "Some generic animal sound"

# Potomek - třída Dog, která dědí Animals
class Dog(Animals):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)  # Voláme konstruktor rodiče

    def makeSound(self):
        return "Woof! Woof!"

# Vytvoření dvou objektů třídy Dog
dog1 = Dog("Rex", 5, 50)
dog2 = Dog("Buddy", 3, 40)

# Výpis jednoho atributu
print("Jméno psa:", dog1.name)

# Vyvolání metody makeSound
print("Zvuk psa:", dog1.makeSound())