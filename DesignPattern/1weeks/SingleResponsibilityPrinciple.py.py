# Single Responsibility Principle
def add(num1, num2):
    return num1 + num2
def numPrint(num):
    print(num)

# Not Single Responsibility Principle
def add(num1, num2):
    num = num1 + num2
    print(num)
    return 

