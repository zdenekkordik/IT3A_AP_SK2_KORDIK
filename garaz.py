import random
from datetime import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int, stkYear:int, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stkYear = stkYear
        self.fuel = fuel
        pass

    def __str__(self): #metoda, která se volá jako základní pro výpis vlastnosti
        return f"{self.brand} {self.model} {(self.year)} - palivo: {self.fuel} %"

    def move(self):
        usage = random.randint(5,20)
        if self.fuel >= usage:
            #self.fuel = self.fuel - usage
            self.fuel -= usage
            return f"{self.brand} {self.model} spotřeboval {usage} a zbývá mu {self.fuel}"
        else:
            return f"{self.brand} {self.model} by do cíle nedojel. Potřebuje {usage} % paliva, ale má jen {self.fuel} % paliva"
        pass

    def fullFill(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.brand} {self.model} natankoval {filled} % paliva."

    def STK(self):
        if self.stkYear <datetime.now().year:
            return f"{self.brand} {self.model} musí na technickou - technická skončila v roce {self.stkYear}"
        else:
            return f"{self.brand} {self.model} má technickou v pořádku. Na technickou bude muset za následující počet let: {self.stkYear - datetime.now().year}"



car1 = Car("Škoda" , "Octavia 3", 2016, 2026, 85)
car2 = Car("Volkswagen" , "Golf 7", 2018, 2022, 10)
car3 = Car("Toyota", "Hilux", 2014, 2028, 3)

#testovací výpis
print(car1)
print(car2)
print(car3)
print(40*"=")

#testovací jízdy
print(car1.move())
print(car2.move())
print(car3.move())
print(40*"=")

print(car3.fullFill())
print(40*"=")

#test stk
print(car1.STK())
print(car2.STK())
print(car3.STK())
print(40*"=")

class Garage: 
    def __init__(self, name):
        self.name = name
        self.cars = []
        pass

    def addCar(self, car:Car):
        self.cars.append(car)
        return f"Do garáže {self.name} bylo přidáno auto: {car.brand} {car.model}"

    def showCars(self):
        if len(self.cars) == 0:
            print(f"Garáž {self.name} je prázdná!")
        else:
            print(f"Auta v garáží {self.name}: ")
            for car in self.cars:
                print("-->", car)

    def oldestCar(self):
        if len(self.cars) == 0:
            return None
        theOldest = min(self.cars, key= lambda a: a.year)
        return theOldest

    def avgFuel(self):
        if len(self.cars) == 0:
            return 0
        return sum(car.fuel for car in self.cars) / len(self.cars)

garage = Garage("Podzemní garáž")

garage.showCars()
print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))
garage.showCars()
print(f"{garage.avgFuel():.1f} %")
oldest = garage.oldestCar()
if oldest:
    print(f"Nejstarší auto v garáží je {oldest.brand} {oldest.model} {oldest.year}")
print(garage.cars[2].move())

for brambora in garage.cars:
    print(brambora.STK())