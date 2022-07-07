import sys


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0:
            return -1
        else:
            self.arr.pop()

    def size(self):
        print(len(self.arr))

    def empty(self):
        if len(self.arr) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]


n = int(sys.stdin.readline())


for _ in range(n):
    par = input()
    # print(par)
    s = Stack()
    for i in par:
        # print(i)
        if i == '(':
            s.push(i)
        elif i == ')':
            top = s.top() # )를 스택에 넣기전 스택에 가장 마지막 원소
            s.push(i)
            if top == '(': #마지막 원소가 (였으면 ),( 둘다 팝해줌
                s.pop()
                s.pop()
    if s.empty():
        print("YES")
    else:
        print("NO")
