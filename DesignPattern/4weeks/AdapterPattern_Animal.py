class Animal:
    def walk(self):
        pass

class Cat(Animal):
    def walk(self):
        print("cat walking")

class Dog(Animal):
    def walk(self):
        print("dog walking")

def makeWalk(animal: Animal):
    animal.walk()

class Fish:
    def swim(self):
        print("fish swimming")

class FishAdapter(Animal):
    def __init__(self,fish:Fish):
        self.fish = fish
    def walk(self):
        self.fish.swim()

kitty = Cat()
bingo = Dog()

makeWalk(kitty)
makeWalk(bingo)

nemo = Fish()
adapted_nemo = FishAdapter(nemo)
makeWalk(adapted_nemo)