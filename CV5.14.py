import re

class Zbozi:
    def __init__(self, nazev: str, vaha: float):
        """
        Pri vytvoreni se nastavuje nazev zbozi a jeho vaha
        :param nazev: Nazev musi byt znaky v rozsahu 1 az 200 znaku
        :param vaha: Vaha musi byt kladne a nenulove cislo
        """
        if not re.match(r"^[a-zA-Z ]{1,200}$", nazev):
            raise Exception('Nazev musi byt v rozsahu 1 az 200 znaku')
        if vaha <= 0:
            raise Exception('Vaha nesmi byt zapojna')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        """
        Metoda zjistuje jestli je zbozi mensi nez druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self mensi nez other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha < other._vaha

    def __gt__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha > other._vaha

    def __le__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha <= other._vaha

    def __ge__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha >= other._vaha

    def __eq__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha == other._vaha

    def __ne__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')
        return self._vaha != other._vaha

kilo_brambor = Zbozi("Brambory", 1)
krabice_mleka = Zbozi("Mleko", 1.029)

if kilo_brambor < krabice_mleka:
    print("kilo_brambor je mensi nez krabice_mleka")
if kilo_brambor > krabice_mleka:
    print("kilo_brambor je vetsi nez krabice_mleka")
if kilo_brambor <= krabice_mleka:
    print("kilo_brambor je mensi nebo rovno krabice_mleka")
if kilo_brambor >= krabice_mleka:
    print("kilo_brambor je vetsi nebo rovno krabice_mleka")
if kilo_brambor == krabice_mleka:
    print("kilo_brambor je stejny jako krabice_mleka")
if kilo_brambor != krabice_mleka:
    print("kilo_brambor neni stejny jako krabice_mleka")
