class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air!!")

class Car(Vehicle):
    def sayHello(self):
        print("Hello Worlds")
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car2 = Pickup()
car2.turnOnAirConditioner()
car3 = Van()
car3.turnOnAirConditioner()
car4 = Estatecar()
car4.turnOnAirConditioner()