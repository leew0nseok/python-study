# 1912, 연속합
n = int(input())
arr = list(map(int, input().split()))


def maxSum(arr, n):
  DP = [0] * n
  DP[0] = arr[0]
  for i in range(1, n):
    DP[i] = max(DP[i-1] + arr[i], arr[i])
  return max(DP)

print(maxSum(arr, n))