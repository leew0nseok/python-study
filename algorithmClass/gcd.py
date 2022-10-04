def gcd(a, b):
  while a * b != 0:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a + b

#재귀
def gcd1(a, b):
  if a == 0 or b == 0:
    return a+b
  if a > b:
    return gcd1(a % b, b)
  else:
    return gcd1(a, b % a)

#재귀
def gcd2(a, b):
  if a == 0 or b == 0:
    return a+b
  return gcd2(b, a % b)



print(gcd(36,24))
print(gcd1(36,24))
print(gcd2(36,24))