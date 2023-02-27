#계단오르기 문제
n = int(input()) #n층의 계단

def upStair(n): #1칸씩, 2칸씩 올라갈 수 있음.
  DP = [0] * (n+1)
  DP[1], DP[2] = 1, 1 #DP[1] = 1층의 경우의 수, DP[2] = 2층의 경우의 수
  for i in range(3, n+1):
    DP[i] = DP[i-1] + DP[i-2]
  return DP[n]
print(upStair(n))