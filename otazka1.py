cisla = (input("Zadejte cisla:"))

cisla = list(map(int, cisla.split()))
cisla.sort()

print(cisla)