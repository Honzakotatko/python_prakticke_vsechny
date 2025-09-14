class NespravneHesloError(Exception):
    """Výjimka pro špatně zadané heslo 3x po sobě."""
    pass


spravne_heslo = "tajne123"
pocet_pokusu = 0

while pocet_pokusu < 3:
    zadane = input("Zadej heslo: ")

    if zadane == spravne_heslo:
        print("Přístup povolen ✅")
        break
    else:
        print("Špatné heslo ❌")
        pocet_pokusu += 1

        if pocet_pokusu == 3:
            raise NespravneHesloError("3x špatně zadané heslo!")