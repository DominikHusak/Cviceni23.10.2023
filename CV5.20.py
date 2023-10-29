class KonfiguraceKonference:
    _maximalni_pocet_ucastniku = 0

    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        """
        Nastaví maximální počet účastníků konference.

        :param max: Maximální počet účastníků
        """
        cls._maximalni_pocet_ucastniku = max

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        """
        Vrátí maximální počet účastníků konference.

        :return: Maximální počet účastníků
        """
        return cls._maximalni_pocet_ucastniku

    def __new__(cls, *args, **kwargs):
        """
        Zamezí vytváření instancí třídy KonfiguraceKonference.
        """
        raise Exception("Nelze vytvářet instance třídy KonfiguraceKonference")

print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

KonfiguraceKonference.set_maximalni_pocet_ucastniku(212)
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

try:
    mojeKonfigurace = KonfiguraceKonference()
    mojeKonfigurace.set_maximalni_pocet_ucastniku(300)
    print(mojeKonfigurace.get_maximalni_pocet_ucastniku())
except Exception as e:
    print(f"Chyba: {e}")
