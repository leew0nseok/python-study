# 원칙을 따르지 않은 코드
class CarBoat:
    def drive():
        pass
    def driveL():
        pass
    def driveR():
        pass
    def steer():
        pass
    def steerL():
        pass
    def steerR():
        pass

class Genesis(CarBoat):
    def drive():
        pass
    def driveL():
        pass
    def driveR():
        pass

class Amphicar(CarBoat):
    def drive():
        pass
    def driveL():
        pass
    def driveR():
        pass
    def steer():
        pass
    def steerL():
        pass
    def steerR():
        pass

class Cruise(CarBoat):
    def steer():
        pass
    def steerL():
        pass
    def steerR():
        pass

##############################
# 원칙을 따른 코드
class Car:
    def drive():
        pass
    def driveL():
        pass
    def driveR():
        pass

class Boat:
    def steer():
        pass
    def steerL():
        pass
    def steerR():
        pass

class Genesis(Car):
    def drive():
        pass
    def driveL():
        pass
    def driveR():
        pass

class Amphicar(Car, Boat):
    def drive():
        pass
    def driveL():
        pass
    def driveR():
        pass
    def steer():
        pass
    def steerL():
        pass
    def steerR():
        pass

class Cruise(Boat):
    def steer():
        pass
    def steerL():
        pass
    def steerR():
        pass