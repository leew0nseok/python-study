class Cat():
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def print(self):
        return print(f"{self.height}cm, {self.width}kg, {self.color}")
    
# Builder
class CatBuilder:

    def __init__(self):
        self.height = None
        self.width = None
        self.color = None

    def setHeight(self, height):
        self.height = height
        return self
    def setWidth(self, width):
        self.width = width
        return self
    def setColor(self, color):
        self.color = color
        return self
    
    def build(self):
        cat = Cat(self.height, self.width, self.color)
        return cat

# Concreate Builder
class WhiteCatBuilder(CatBuilder):
    def __init__(self):
        super().__init__()
        self.color = 'white'

# Concreate Builder
class BlackCatBuilder(CatBuilder):
    def __init__(self):
        super().__init__()
        self.color = 'black'

white_cat = WhiteCatBuilder().setHeight(10).setWidth(3).build()
black_cat = BlackCatBuilder().setHeight(15).setWidth(2).build()

white_cat.print()
black_cat.print()