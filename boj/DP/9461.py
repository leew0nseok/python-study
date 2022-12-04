# 9461, 파도반 수열

t = int(input())

for i in range(t):
  n = int(input())
  DP = [0] * (n+1)
  DP[1], DP[2], DP[3] = 1, 1, 1
  for j in range(4, n+1):
    DP[i] = DP[i-3] + DP[i-2]
  print(DP[n])