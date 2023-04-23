# Implementation
class Power:
    def powerUp(self):
        pass

    def powerDown(self):
        pass

class Gas(Power):
    def powerUp(self):
        return "Gas power up"
    
    def powerDown(self):
        return "Gas power down"
    
class Disel(Power):
    def powerUp(self):
        return "Disel power up"
    
    def powerDown(self):
        return "Disel power down"

class Motor(Power):
    def powerUp(self):
        return "Motor power up"
    
    def powerDown(self):
        return "Motor power down"

# Abstractaction
class Car:
    def __init__(self, power:Power):
        self.power = power
    
    def drive(self):
        pass

    def stop(self):
        pass

class Sedan(Car):
    def drive(self):
        print("Sedan drive with " + self.power.powerUp())

    def stop(self):
        print("Sedan stop with " + self.power.powerDown())

class SUV(Car):
    def drive(self):
        print("SUV drive with " + self.power.powerUp())

    def stop(self):
        print("SUV stop with " + self.power.powerDown())

class Truck(Car):
    def drive(self):
        print("Truck drive with " + self.power.powerUp())

    def stop(self):
        print("Truck stop with " + self.power.powerDown())


diselcar = Disel()
truck = Truck(diselcar)

truck.drive()
truck.stop()