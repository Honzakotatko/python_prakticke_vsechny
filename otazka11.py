"""
# Otevření souboru pro zápis
with open("texty.txt", "w", encoding="utf-8") as file:
    for i in range(5):
        text = input(f"Zadej {i+1}. text: ")
        file.write(text + "\n")  # Uložení textu do souboru

print("Texty byly úspěšně uloženy do souboru texty.txt.")
"""

seznam = []

with open("texty.txt", "w", encoding="utf-8") as file:
    for i in range(5):
        vstup = (input("Zadejte text: "))
        seznam.append(vstup)
        
    file.write("\n".join(seznam))