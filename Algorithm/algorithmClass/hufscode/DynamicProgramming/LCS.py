#LCS(Longest Common Subsequence)문제

X = str(input())
Y = str(input())

def LCS(X, Y):
  n, m = len(X), len(Y)
  DP= [[0]*(m+1) for i in range(n+1)] 
  for j in range(0, m+1):
    DP[0][j] = 0
  for i in range(0, n+1):
    DP[i][0] = 0
  
  for i in range(1, n+1):
    for j in range(1, m+1):
      if X[i-1] == Y[j-1]: #마지막 글자가 같음
        DP[i][j] = DP[i-1][j-1] + 1
      else: #마지막 글자가 다름
        DP[i][j] = max(DP[i-1][j], DP[i][j-1])
  return DP[n][m]

print(LCS(X, Y))