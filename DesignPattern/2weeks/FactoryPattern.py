from enum import Enum

class RobotEnum(Enum):
    CAT = 0
    DOG = 1

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

    def makeRobot(self, robot:RobotEnum):
        if robot == RobotEnum.CAT:
            return Cat()
        elif robot == RobotEnum.DOG:
            return Dog()
        

fac1 = RobotFactory()
dog = fac1.makeRobot(RobotEnum.DOG)
dog.speak()
cat = fac1.makeRobot(RobotEnum.CAT)
cat.speak()