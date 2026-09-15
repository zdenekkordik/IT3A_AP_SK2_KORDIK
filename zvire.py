class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

    def zvuk(self):
        return"???"


    def predstavSe(self):
        return f"Jsem {self.jmeno} a je mi {self.vek}"

    def kdeJsi(self):
        return f"Jsem v místě zvaném {self.misto}"

    def jdiNa(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}"
    
zvire = Zvire("Šoral",50)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)
print(zvire.predstavSe())
print(zvire.kdeJsi())
print(zvire.jdiNa("Kadeřnictví"))


print(zvire.zvuk())


zvire2= Zvire("Wolfram", 32, "PentHouse")
print(zvire2.jmeno)
print(zvire2.predstavSe())
print(zvire2.kdeJsi())
print(zvire2.jdiNa("Klokánek"))



