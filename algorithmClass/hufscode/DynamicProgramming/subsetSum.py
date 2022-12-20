# DP로 푼 subsetSum
def solve_DP(A, S): # each A[i] > 0 and S > 0
  n = len(A)
  DP = [[0 for s in range(S+1) for _ in range(n)]]
  for i in range(0, n):
    for s in range(1, S+1):
      DP[i][s] = DP[i-1][s]
      if s > A[i]:
        DP[i][s] += DP[i-1][s-A[i]]
      elif s == A[i]:
        DP[i][s] += 1
  return DP[n-1][S]

A = [int(x) for x in input().split()]
S = int(input())     
print(solve_DP(A, S))