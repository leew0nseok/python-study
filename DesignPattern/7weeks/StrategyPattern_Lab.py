from abc import *
# 뛰거나 걸을 수 있는 "움직일 수 있는 기능" strategy1
class Move(metaclass = ABCMeta): 
    @abstractmethod
    def moving(self):
        pass

class Run(Move):
    def moving(self):
        print("달린다.\n")

class Walk(Move):
    def moving(self):
        print("걷는다.\n")

class Fly(Move):
    def moving(self):
        print("난다.\n")

# 총을 쏘거나 로켓을 발사할 수 있는 " 공격할 수 있는 기능" strategy2
class Attack(metaclass = ABCMeta):
    def attacking(self):
        pass

class ShootGun(Attack):
    def attacking(self):
        print("총을 쏜다.\n")

class LaunchRocket(Attack):
    def attacking(self):
        print("로켓 발사.\n")

# context
class Robot:
    def __init__(self):
        self.move_strategy = None
        self.attack_strategy = None
        
    def setMove(self, move: Move):
        self.move_strategy = move
        
    def setAttack(self, attack: Attack):
        self.attack_strategy = attack

    def move(self):
        self.move_strategy.moving()

    def attack(self):
        self.attack_strategy.attacking()

robot = Robot()

robot.setMove(Run())
robot.move()

robot.setMove(Fly())
robot.move()

robot.setAttack(ShootGun())
robot.attack()

robot.setAttack(LaunchRocket())
robot.attack()
