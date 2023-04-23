# 강의 자료와 구현, 기능을 하는 클래스를 반대로 작성해봄.

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("drives a car")

class Boat(Vehicle):
    def start(self):
        print("drives a boat")

class Airplane(Vehicle):
    def start(self):
        print("drives a airplane")

class Animal:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print(" a cat ", end="")
        self.vehicle.start()

class Dog(Animal):
    def speak(self):
        self.vehicle.start()
        print(" a dog ", end="")
        self.vehicle.start()


boat = Boat()
cat = Cat(boat)
cat.speak()