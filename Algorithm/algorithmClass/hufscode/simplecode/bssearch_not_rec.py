def BS(A, k):
  left, right = 0, len(A)
  while left - right <=0:
    m = (left + right)//2
    if A[m] > k:
      right = m -1
    elif A[m] < k:
      left = m +1
    else:
      return m
    
A = [1, 3, 5, 7, 8, 9, 11]
print(BS(A, 5))