import random

def quick_sort_insertion(A, first, last):
  global Qsi, Qci
  k = 20
  if first >= last: 
    return
  elif last - first < k:
    for i in range(last - first + 1): # (5, 25)
      for j in range(i,0,-1):
        Qci += 1
        if A[first+j] < A[first+j-1]:
          Qsi += 1
          A[first+j], A[first+j-1] = A[first+j-1], A[first+j]
        else:
            break
    return
  left, right = first+1, last
  pivot = A[first]
  while left <= right:
    while left <= last and A[left] < pivot:
      Qci += 1
      left += 1
    while right > first and A[right] > pivot:
      Qci += 1
      right -= 1
    if left <= right:
      Qsi += 1
      A[left], A[right] = A[right], A[left]
      left += 1
      right -= 1
  
  A[first], A[right] = A[right], A[first]
  Qsi += 1
  quick_sort_insertion(A, first, right-1)
  quick_sort_insertion(A, right+1, last)

A = []

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
n = len(A)

# random.seed()

# for i in range(n):
#     A.append(random.randint(-1000,1000))

print(A)
quick_sort_insertion(A, 0, n -1)
print(A)