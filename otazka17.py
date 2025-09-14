import threading
import time

# Funkce pro výpočet součtu čísel od 1 do N
def secti_cisla(n):
    time.sleep(1)  # Zpoždění výpočtu o 1 sekundu
    soucet = sum(range(1, n + 1))
    print(f"Součet čísel od 1 do {n} je {soucet}")

# Vytvoření dvou vláken s různými hodnotami N
vlakno1 = threading.Thread(target=secti_cisla, args=(10,))
vlakno2 = threading.Thread(target=secti_cisla, args=(20,))

# Spuštění vláken
vlakno1.start()
vlakno2.start()

# Počkáme na dokončení obou vláken
vlakno1.join()
vlakno2.join()

# Výpis po dokončení práce
print("Konec práce")
