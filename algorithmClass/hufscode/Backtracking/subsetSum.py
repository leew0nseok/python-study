# Backtracking SubsetSum 문제
A = [8, 6, 7, 5, 3, 10, 9]
X = [0] * len(A)
S = 15
current_sum = 0

def subsetSum(k):
  # global A, X, S
  current_sum = 0
  for i in range(len(X)):
    if X[i] == 1:
      current_sum += A[i]
  if k >= len(A):
    if current_sum == S:
      print(X) 
  else:
    if current_sum + A[k] <= S:
      X[k] = 1
      subsetSum(k+1)
    X[k] = 0
    subsetSum(k+1)

subsetSum(0)

print(X)