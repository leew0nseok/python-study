#DP 최대구간 합 문제
A = list(map(int, input().split()))

def maxSum(A):
  DP = [0] * len(A)
  DP[0] = A[0]
  for i in range(1, len(A)):
    DP[i] = max(A[i], DP[i-1] + A[i])
  return DP

print(max(maxSum(A)))