# Postfix-Evaluation
class Stack:
    def __init__(self):
        self.data = []  # initialize with an empty list

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0  # True if empty, False otherwise

    def push(self, a):
        self.data.append(a)

    def pop(self):
        if self.is_empty():
            return "error"
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return "error"
        return self.data[-1]


postfix = str(input())
s = Stack()
# precedence = {'+' : 0, '-' : 0, '*' : 1, '/' : 1, '(' : 2}

for c in postfix:
    if c not in '+-*/(':  # 연산자가 아닐경우 스택에 숫자 넣기
        s.push(int(c))
    else:  # 연산자 일경우
        if c == '+':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 + op1)
        elif c == '-':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 - op1)
        elif c == '*':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 * op1)
        elif c == '/':
            op1 = s.pop()
            op2 = s.pop()
            s.push(op2 / op1)

print(s.pop())
