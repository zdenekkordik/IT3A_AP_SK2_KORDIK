import random
from datetime import datetime

class Animal:
    def __init__(self, species:str, name:str, birthYear:int, checkupYear:int = 0, energy:int = 100):
        self.species = species
        self.name = name
        self.birthYear = birthYear
        self.checkupYear = checkupYear
        self.energy = energy
        pass

    def __str__(self):
        return f"{self.species} {self.name} {self.birthYear} - energie: {self.energy} %"

    def play(self):
        usage = random.randint(5,20)
        if self.energy >= usage:
            self.energy-= usage
            return f"{self.species} {self.name} spotřeboval při hře {usage}% energie a zbývá mu {self.energy}"
        else:
            return f"{self.species} {self.name} je moc unavený. Potřebuje {usage}% energie, ale má jen {self.energy}%"
        pass

    def feed(self):
        filled = 100 - self.energy  
        self.energy = 100
        return f"{self.species} {self.name} byl nakrmen a doplnil {filled}% energie."

    def vetCheck(self):
        if self.checkupYear <datetime.now().year:   
            return f"{self.species} {self.name} musí k veterinářovi - platnost prohlídky skončila v roce {self.checkupYear}"
        else:
            return f"{self.species} {self.name} má prohlídku v pořádku. Další kontrola bude za následující počet let: {self.checkupYear - datetime.now().year}"


animal1 = Animal("Lev", "Alex", 2016, 2026, 85)
animal2 = Animal("Zebra", "Marty", 2018, 2022)
animal3 = Animal("Žirafa", "Melman", 2014, 2028, 10)
animal4 = Animal("Lev", "Simba", 2020, 2024, 40)

print(animal1)
print(animal2)
print(animal3)
print(animal4)
print(40*"=")

print(animal1.play())
print(animal2.play())
print(animal3.play())
print(animal4.play())
print(40*"=")

print(animal1.feed())
print(animal2.feed())
print(animal3.feed())
print(animal4.feed())
print(40*"=")

print(animal1.vetCheck())
print(animal2.vetCheck())
print(animal3.vetCheck())
print(animal4.vetCheck())
print(40*"=")

class Zoo:
    def __init__(self, nazev):
        self.nazev = nazev
        self.animals = []
        pass

    def addAnimal(self, animal:Animal):
        self.animals.append(animal)
        return f"Do {self.nazev} bylo přidáno zvíře {animal.species} {animal.name}"

    def showAnimal(self):
        if len(self.animals) == 0:
            print(f"{self.nazev} je prázdná!")
        else:
            print(f"Zvířata v {self.nazev}: ")
            for animal in self.animals:
                print("-->", animal)