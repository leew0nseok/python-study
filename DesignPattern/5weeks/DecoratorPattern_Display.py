# Component
class Display():

    def getColums(self):
        pass
    def getRows(self):
        pass
    def getRowText(self, row):
        pass

    def show(self):
        n = self.getRows()
        for i in range(n):
            print(self.getRowText(i))

# Concreate Component
class StringDisplay(Display):
    def __init__(self, letters):
        self.letters = letters
    
    def getColums(self):
        return len(self.letters)
    def getRows(self):
        return 1
    def getRowText(self, row):
        if row == 0:
            return self.letters
        else:
            return -1
        
# Decorator
class Deco(Display):
    def __init__(self,display:Display):
        self.display = display

# Concreate Decorator 1
class SideBorder(Deco):
    def __init__(self,display, deco):
        super().__init__(display)
        self.borderDeco = deco

    def getColums(self):
        return 1 + self.display.getColums() + 1
    def getRows(self):
        return self.display.getRows()
    def getRowText(self, row):
        return self.borderDeco + self.display.getRowText(row) + self.borderDeco

# Concreate Decorator 2
class FullBorder(Deco):
    def __init__(self,display):
        super().__init__(display)

    def getColums(self):
        return 1 + self.display.getColums() + 1
    def getRows(self):
        return 1 + self.display.getRows() + 1
    
    def makeLine(self, deco, count):
        buffer = ""
        for i in range(count):
            buffer += deco
        return buffer
    def getRowText(self, row):
        if row == 0:
            return "+" + self.makeLine("-", self.display.getColums()) + "+"
        elif row == (self.display.getRows() + 1): #인덱스 -> 개수
            return "+" + self.makeLine("-", self.display.getColums()) + "+"
        else:
            return "ㅣ" + self.display.getRowText(row-1) + "ㅣ"
        
b1 = StringDisplay("Hello")
b2 = SideBorder(b1, "!")
b3 = FullBorder(b2)
b1.show()
b2.show()
b3.show()
c1 = SideBorder(b3, "*")
c1.show()
c2 = FullBorder(c1)
c2 = FullBorder(c2)
c2.show()