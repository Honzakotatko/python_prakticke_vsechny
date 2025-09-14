class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - {self.price} Kč"

class PhoneFactory:
    @staticmethod
    def create_phone(brand, model, price):
        return Phone(brand, model, price)

# Použití Factory
phone1 = PhoneFactory.create_phone("Apple", "iPhone 15", 29999)
phone2 = PhoneFactory.create_phone("Samsung", "Galaxy S24", 25999)

print(phone1)
print(phone2)