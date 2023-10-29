class Zbozi:
    def __new__(cls, nazev, cena):
        if not isinstance(nazev, str) or cena < 0 or not isinstance(cena, (int, float)):
            instance = None
        else:
            instance = super().__new__(cls)
        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

a = Zbozi("Rohlik", 5)
b = Zbozi("Hackers item", -10)
c = Zbozi(42, 10)  # Vyhodí chybu
print(a)
print(b)
print(c)