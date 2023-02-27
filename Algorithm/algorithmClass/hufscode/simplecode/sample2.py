a = []

for i in range(6):
  if i %2: a.append(2*i)
  else: a.append(2*i-1)
print(a)
a.pop()
a.pop(0)
print(a)
a.insert(2,9)
print(a)