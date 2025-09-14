def pridej_prvek(pole, prvek):
    pole.append(prvek)
    
def vytvor_hashe(pole):
    for prvek in pole:
        print(prvek, "->", hash(prvek))
        
        
pole = ["a", "b", "c", 5, 8]
print(f"Puvodni pole: {pole}")

novy = input("Zadej novy prvek: ")
pridej_prvek(pole, novy)

print("\nHash hodnoty jednotlivych prvku: ")
vytvor_hashe(pole)

