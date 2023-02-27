import sys


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0:
            print(-1)
        else:
            print(self.arr.pop())

    def size(self):
        print(len(self.arr))

    def empty(self):
        if len(self.arr) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.arr) == 0:
            print(-1)
        else:
            print(self.arr[-1])


n = int(sys.stdin.readline())


for _ in range(n):
    sentense = sys.stdin.readline().split()
    s = Stack()
    for i in sentense:
        s.push(i)
    for j in s.arr:
        for x in range(len(j)):
            print(j[len(j) - (x+1)], end='')
        print(end=" ")