#DP 최대구간 합 문제
A = list(map(int, input().split()))

#A = [1, -1, 3, -4, 5, -4, 6, -2]
#1. 단순한 방법
def simplecode(A):
  maxVal = A[0]
  for i in range(len(A)):
    for j in range(len(A)):
      if (i <= j):
        S = sum(A[i:j])
        if maxVal < S: maxVal = S
  return maxVal
    
# 2. prefixsum
def prefixsum(A):
  P =[0] * (len(A))
  P[0] = A[0]
  for i in range(1, len(A)):
    P[i] = P[i-1] + A[i]

  for i in range(len(A)):
    for j in range(len(A)):
      if (i <= j):
        S = P[j] - P[i-1]
  return max(P)

# 3. Divide&Conquer

def dc(A, left, right):
  if left >= right: return A[left]
  m = (left + right)//2
  L = dc(A, left, m)
  R = dc(A, m+1, right)
  # m부터 왼쪽 구간 최대 합
  sum = 0
  leftmax = A[m]
  for i in range(m, left-1, -1):
    sum += A[i]
    leftmax = max(sum, leftmax)
  # m+1부터 오른쪽 구간 최대 합
  sum = 0
  rightmax = A[m+1]
  for i in range(m+1, right+1):
    sum += A[i]
    rightmax = max(sum, rightmax)
  M = leftmax + rightmax
  
  return max(L, M, R)
    

# 4. DP
def maxSum(A):
  DP = [0] * len(A)
  DP[0] = A[0]
  for i in range(1, len(A)):
    DP[i] = max(A[i], DP[i-1] + A[i])
  return DP

print(simplecode(A))
print(prefixsum(A))
print(dc(A, 0, len(A)-1))
print(max(maxSum(A)))