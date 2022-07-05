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

s = Stack()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'size':
        s.size()
    elif cmd[0] == 'top':
        s.top()
    elif cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'empty':
        s.empty()
    elif cmd[0] == 'push':
        s.push(cmd[1])