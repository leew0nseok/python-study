def arrayMax(A, n):
  max = A[0]
  for i in range(1, n):
    if A[i] > max:
      max = A[i]
    return max

  
