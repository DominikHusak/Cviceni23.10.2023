class Zbozi:
    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi " + str(self.nazev) + " bylo vymazáno z paměti")

z = Zbozi("Banan")
me_oblibene_zbozi = z  #odkazují na stejný objekt
del z  # smaže proměnnou z, ale objekt v paměti zůstává
