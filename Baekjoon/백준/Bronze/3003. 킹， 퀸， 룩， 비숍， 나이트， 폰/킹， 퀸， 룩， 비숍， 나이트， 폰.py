data = list(map(int, input().split()))
need = list()
for i in range(2):
  need.append(1 - data[i])
for i in range(2, 5):
  need.append(2- data[i])
need.append(8 - data[-1])

for i in range(len(need)):
  print(need[i], end=' ')