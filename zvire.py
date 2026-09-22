import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

    def zvuk(self):
        return "???"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno} a je mi {self.vek}"

    def kdeJsi(self):
        return f"Jsem v místě zvaném {self.misto}"

    def jdiNa(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}"
    
    
class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return "Haf, haf!"
    
    def aport(self):
        return f"{self.jmeno} přinesl míček!"
    
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před tvým kartáčem!"
        else:
            return f"{self.jmeno} se nechal vyčesat!"
    
    def predstavSe(self):
        return f"{super().predstavSe()} jsem {self.plemeno}"
    

class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva

    def zvuk(self):
        return "Mňau, mňau!"
    
    def utok(self):
        return f"Kočka {self.jmeno} tě poškrábala"
    
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return self.utok()
        else:
            return f"{self.jmeno} se nechala pohladit a spokejeně přede!"
        

class Had(Zvire):
    def __init__(self, jmeno, vek, delkaCm: int, jedovaty:bool, misto = "terarium"):
        super().__init__(jmeno, vek, misto)
        self.delkaCm = delkaCm
        self.jedovaty = jedovaty

    def zvuk(self):
        return "Sssssss"
    
    def predstavSe(self):
        if self.jedovaty:
            typ = "jedovaty"
        else:
            typ = "škrtič"
        return f"Ssssss já jsem {self.jmeno}, měřím {self.delkaCm} cm a jsem {typ}"

betka = Had("Bětka", 8, 250, False)
print(betka.predstavSe())

micka = Kocka("Micka", 3, "zrzavou", "košíček")
print(micka.jmeno)
print(micka.kdeJsi())
print(micka.zvuk())
print(micka.utok())
print(micka.pohladit())
print(micka.predstavSe())
print("-" * 20)


radegast = Pes("Radegast", 2, "Australský ovčák", "gauč")
print(radegast.jmeno)
print(radegast.plemeno)
print(radegast.kdeJsi())
print(radegast.zvuk())
print(radegast.aport())
print(radegast.vycesat())
print("-" * 20)


zvire = Zvire("Šoral",50)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)
print(zvire.zvuk())
print(zvire.predstavSe())
print(zvire.kdeJsi())
print(zvire.jdiNa("Kadeřnictví"))
print(zvire.kdeJsi())

zvire2 = Zvire("Wolfram", 32, "PentHouse")
print(zvire2.jmeno)
print(zvire2.predstavSe())
print(zvire2.kdeJsi())
print(zvire2.jdiNa("Klokánek"))
print(zvire2.kdeJsi())

zoo = [radegast, micka, betka]

for obyvatel in zoo:
    print(obyvatel.predstavSe())
    print(obyvatel.zvuk())
    print("-" * 20)
