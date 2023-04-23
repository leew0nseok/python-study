"""
# 상속사용
# target 
class Print:
    def __init__(self, msg):
        self.msg = msg

    def printStrong(self):
        print("print strong " + self.msg)
    
    def printWeek(self):
        print("print week " + self.msg)

# Adaptee
class Banner:
    def __init__(self, msg):
        self.msg = msg

    def printStar(self):
        print('*' + self.msg + '*')
    
    def printParen(self):
        print('(' + self.msg + ')')

# Adapter 
class PrintBanner(Banner, Print):

    def __init__(self, msg):
        super(PrintBanner, self).__init__(msg)
    
    def printStrong(self):
        self.printStar()

    def printWeek(self):
        self.printParen()"""

# 위임 사용
# target 
class Print:
    def __init__(self, msg):
        self.msg = msg

    def printStrong(self):
        print("print strong " + self.msg)
    
    def printWeek(self):
        print("print week " + self.msg)

# Adaptee
class Banner:
    def __init__(self, msg):
        self.msg = msg

    def printStar(self):
        print('*' + self.msg + '*')
    
    def printParen(self):
        print('(' + self.msg + ')')

# Adapter 
class PrintBanner(Print):

    def __init__(self, msg):
        self.banner = Banner(msg)
    
    def printStrong(self):
        self.banner.printStar()

    def printWeek(self):
        self.banner.printParen()

pb = PrintBanner("Hello")
pb.printStrong()
pb.printWeek()