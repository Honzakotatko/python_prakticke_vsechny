seznam = []

for x in range(5):
    vstup = int(input("Zadejte cislo:"))
    seznam.append(vstup)
    
# Bubble sort
    for i in range(len(seznam)):
        for j in range(len(seznam) - 1):
            if seznam[j] > seznam[j + 1]:
            # Prohození prvků
                seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]

print(seznam)