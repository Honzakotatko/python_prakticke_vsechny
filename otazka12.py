# Definice třídy Film
class Film:
    def __init__(self, nazev, rok, zanr):
        self.nazev = nazev
        self.rok = rok
        self.zanr = zanr

    def __str__(self):
        return f"{self.nazev} ({self.rok}) - {self.zanr}"

# Vytvoření slovníku pro filmy
filmy = {}

# Přidání 5 filmů do slovníku
filmy[0] = Film("Pán prstenů", 2001, "Fantasy")
filmy[1] = Film("Matrix", 1999, "Sci-Fi")
filmy[2] = Film("Forrest Gump", 1994, "Drama")
filmy[3] = Film("Gladiátor", 2000, "Historický")
filmy[4] = Film("Inception", 2010, "Sci-Fi")

# Výpis všech filmů
for id, film in filmy.items():
    print(f"ID: {id} -> {film}")