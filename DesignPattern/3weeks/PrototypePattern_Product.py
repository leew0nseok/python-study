from abc import *
import copy
# Prototype
class Product(metaclass = ABCMeta):

    @abstractclassmethod
    def use(self):
        pass

    @abstractclassmethod
    def clone(self):
        pass

# Concreate Prototype
class UnderlinePen(Product):
    def use(self, s:str):

        n = len(s)
        print(s)
        for i in range(n):
            print("~", end="")
        print()

    def clone(self):
        return copy.deepcopy(self)
    
# Concreate Prototype
class MessageBox(Product):
    def __init__(self, deco:str):
        self.deco = deco
    
    def use(self, s:str):
        n = len(s) +4

        for i in range(n):
            print(self.deco, end = "")
        print()
        print(self.deco, s, self.deco)
        for i in range(n):
            print(self.deco, end = "")
        print()
    
    def clone(self):
        return copy.deepcopy(self)
    
class Manager:

    def __init__(self):
        self.showcase = {"a":1}
    
    def register(self, name:str, proto:Product):
        self.showcase[name] = proto
    
    def create(self, protoName):
        p = self.showcase[protoName]
        return p.clone()
    
#### main ###

manager = Manager()

m1 = MessageBox("*")
m2 = MessageBox("#")
p1 = UnderlinePen()

manager.register("msg*", m1)
manager.register("msg#", m2)
manager.register("pen", p1)
msg1 = manager.create("msg*")
msg2 = manager.create("msg#")
pen = manager.create("pen")

word = "Hello"
msg1.use(word)
print()
word= "World"
msg2.use(word)
print()
pen.use(word)