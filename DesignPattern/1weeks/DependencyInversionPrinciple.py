# 의존관계가 Animal 추상클래스에 의해 역전되었고, Zoo 클래스는 각 Cat, Dog 등의 클래스로부터 독립되었음.
"""
                  <- Cat
    Zoo -> Animal <- Dog
                  <- Lion
                  <- Tiger
"""
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")

class Zoo:
    def __init__(self):
        self.animals = []

    def addAnimal(self, animal:Animal):
        self.animals.append(animal)

    def speakAll(self):
        for animal in self.animals:
            animal.speak()