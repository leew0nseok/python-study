#a^n계산하기

from tkinter import Y


def power1(a, n): #O(n)
  if n == 1:
    return a
  return a * power1(a, n-1)

def power2(a, n): #O(n)
  if n == 0: return 1
  if n % 2 == 1: #n이 홀수일때
    return power2(a, n//2) * power2(a, n//2) * a
  else: #n이 짝수
    return power2(a, n//2) * power2(a, n//2)
  
def power3(a, n): #선형 재귀 호출이지만, 빠른방법 O(logN)
  if n == 0: return 1
  p = power3(a, n//2)
  if n % 2 ==1: #n이 홀수
    return p * p * a
  else:
    return p * p
  
def power4(a, n):
  result, power = 1.0, n
  if n < 0:
    power, n = -power, 1.0/a
  while power:
    if power & 1:
      result *= a
    a, power = a * a, power >> 1
  return result


print(power1(2,6))
print(power2(2,6))
print(power3(2,6))
print(power4(2,6))
