cislo = int(input("Zadej cislo: "))

print("cislo je sude") if cislo %2 == 0 else print("cislo je liche")

for i in range(cislo):
    print(" "*(cislo - i) + "*"*(i*2+1))