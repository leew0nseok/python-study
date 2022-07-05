n = int(input())

result = 0

for i in range(1, n+1):
  v = list(map(int, str(i)))
  result = i + sum(v)
  if result == n:
    print(i)
    break
  
  if i == n:
    print(0)