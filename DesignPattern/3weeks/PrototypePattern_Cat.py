"""
class Cat:
    def __init__(self):
        self.color = None
        self.eye_color = None
        self.nose_color = None
        self.tail_color = None
        self.name = None

    def __repr__(self):
        return f"name: {self.name}, color: {self.color}, eye_color: {self.eye_color}, nose_color: {self.nose_color}, tail_color: {self.tail_color}"

kitty = Cat()
kitty.color = "white"
kitty.eye_color = "white"
kitty.nose_color = "white"
kitty.tail_color = "white"
kitty.name = "kitty"

# 안 좋은 코드임. reference가 2개이므로 한개의 Object가 수정됨. 
# 따라서 deepcopy를 사용해야함.
nabi = kitty
nabi.name = "nabi"
print(kitty)
print(nabi)
"""
import copy

# Prototype
class Cat:
    def __init__(self):
        self.color = None
        self.eye_color = None
        self.nose_color = None
        self.tail_color = None
        self.name = None

    def clone(self):
        return copy.deepcopy(self)
    
    def __repr__(self):
        return f"name: {self.name}, color: {self.color}, eye_color: {self.eye_color}, nose_color: {self.nose_color}, tail_color: {self.tail_color}"

# Concreate Prototype
class BlackCat(Cat):
    def __init__(self):
        super().__init__()
        self.color = "black"

# Concreate Prototype
class YellowCat(Cat):
    def __init__(self):
        super().__init__()
        self.color = "yellow"

kitty = YellowCat()
# kitty.color = "white"
kitty.eye_color = "blue"
kitty.nose_color = "white"
kitty.tail_color = "white"
kitty.name = "kitty"

nabi = kitty.clone()
nabi.name = "nabi"

print(kitty)
print(nabi)