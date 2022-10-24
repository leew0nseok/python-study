def sum(a, b):
  if b == a:
    return a
  m = (a + b) // 2
  return sum(a, m) + sum(m+1, b)

print(sum(2,7))