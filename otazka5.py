for _ in range(3):
    cislo = int(input("Zadej číslo: "))

    if cislo < 20:
        print("Číslo je menší než 20.")
    elif 20 <= cislo <= 30:
        print("Číslo je mezi 20 a 30.")
    else:
        print("Číslo je větší než 30.")
        
        
a = 10
b = 20

# Použití ternárního operátoru
minimum = a if a < b else b

print(f"Menší číslo je: {minimum}")