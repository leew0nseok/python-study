#DP를 이용한 피보나치 수열
def fibo(n):
  F = [0] * (n+1)
  F[1] = 1
  
  for i in range(2, n+1):
    F[i] = F[i-2] + F[i-1]
  return F

print(fibo(10))