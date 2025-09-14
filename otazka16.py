"""
import logging
import unittest

logging.basicConfig(filename="aplikace.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(massage)s")

def secti(a, b):
    return a + b

class TestMatematika(unittest.TestCase):
    def test_secti(self):
        logging.debug("Ladici zprava")
        logging.info("Informace")
        logging.warning("Varovani")
        logging.error("Chyba")
        logging.critical("Kritikca chyba")
        self.assertEqual(secti(2, 3), 5)
        self.assertNotEqual(secti(2, 2), 4)

if __name__ == "__main__":
    unittest.main()
"""
# Vlastní výjimka pro špatné heslo
class NespravneHesloError(Exception):
    pass

# Správné heslo
spravne_heslo = "tajne123"

# Počet pokusů
pokusy = 3

# Uživatelský vstup s kontrolou hesla
for i in range(pokusy):
    zadane_heslo = input("Zadej heslo: ")
    if zadane_heslo == spravne_heslo:
        print("Přihlášení úspěšné!")
        break
    else:
        print("Špatné heslo!")
else:
    # Pokud uživatel 3x selže, vyvoláme výjimku
    raise NespravneHesloError("Třikrát špatné heslo! Přístup odepřen.")
