# Component
class Animal:
    def speak(self):
        pass

# Concreate Component
class Cat(Animal):
    def speak(self):
        print("meow", end = "")

# Concreate Component
class Dog(Animal):
    def speak(self):
        print("bark", end = "")

def makeSpeak(animal:Animal):
    animal.speak()
    print(" ")

# Decorator
class Deco(Animal):
    def __init__(self, animal:Animal):
        self.animal = animal
    def speak(self):
        self.animal.speak()

# Concreate Decorator
class WthSmile(Deco):
    def speak(self):
        self.animal.speak()
        print("😃", end = "")

# Concreate Decorator
class WthHeartEyes(Deco):
    def speak(self):
        self.animal.speak()
        print("😍", end = "")

kitty = Cat()
makeSpeak(kitty)
kitty_smile = WthSmile(kitty)
makeSpeak(kitty_smile)
kitty_heart = WthHeartEyes(kitty_smile)
# kitty_heart.speak()
makeSpeak(kitty_heart)