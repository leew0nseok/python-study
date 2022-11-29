def find_max(A, n):
  if n == 1:
    return A[0]
  return max(find_max(A, n-1), A[-1])
  
def reverse(A):
  if len(A) == 1:
    return A
  return reverse(A[1:]) + A[0] #A[0]를 맨 뒤로 보내고 나머지는 재귀