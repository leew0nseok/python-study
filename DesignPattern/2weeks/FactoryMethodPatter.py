
class Robot:
    def speak(self):
        pass

class Cat(Robot):
    def speak(self):
        print("meow")

class Dog(Robot):
    def speak(self):
        print("bark")

class RobotFactory:

    def makeRobot(self):
        pass

class CatFactory(RobotFactory):
    def __init__(self):
        self.cat_count = 0
    
    def makeRobot(self):
        self.cat_count += 1
        return Cat()
    def catCount(self):
        return self.cat_count

class DogFactory(RobotFactory):
    def __init__(self):
        self.dog_count = 0
    
    def makeRobot(self):
        self.dog_count += 1
        return Dog()
    def dogCount(self):
        return self.dog_count

fac1 = DogFactory()
dog = fac1.makeRobot()
dog.speak()
fac2 = CatFactory()
cat = fac2.makeRobot()
cat.speak()