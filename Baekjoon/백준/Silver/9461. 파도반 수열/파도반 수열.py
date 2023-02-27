# 9461, 파도반 수열

t = int(input())

DP = [0] * (101)
DP[1], DP[2], DP[3] = 1, 1, 1
for j in range(4, 101):
  DP[j] = DP[j-3] + DP[j-2]
    
for i in range(t):
  n = int(input())
  print(DP[n])