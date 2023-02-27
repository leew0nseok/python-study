import random

# 3way
def three_merge_sort(A, first, last):
  if last - first < 2:
    return
  three_merge_sort(A, first, first + ((last - first) // 3))
  three_merge_sort(A, first + ((last - first) // 3), first + 2 * ((last - first) // 3) + 1)
  three_merge_sort(A, first + 2 * ((last - first) // 3) + 1, last)

  merge_three_sorted_lists(A, first, last)

def merge_three_sorted_lists(A, first, last):
  m1 = first + ((last - first) // 3)
  m2 = first + 2 * ((last - first) // 3) + 1
  i, j, r= first, m1, m2
  B =[]

  while ((i < m1) and (j < m2) and (r < last)):
    if A[i] < A[j]:
      if A[i] < A[r]:
        B.append(A[i])
        i += 1
      else:
        B.append(A[r])
        r += 1
    else:
      if A[j] < A[r]:
        B.append(A[j])
        j += 1
      else:
        B.append(A[r])
        r += 1

  while ((i < m1) and (j < m2)):
    if A[i] < A[j]:
      B.append(A[i])
      i += 1
    else:
      B.append(A[j])
      j += 1
  while ((j < m2) and (r < last)):
    if A[j] < A[r]:
      B.append(A[j])
      j += 1
    else:
      B.append(A[r])
      r += 1

  while ((i < m1) and (r < last)):
    if A[i] < A[r]:
      B.append(A[i])
      i += 1
    else:
      B.append(A[r])
      r += 1
  for k in range(i, m1):
    B.append(A[k])
    # Ms += 1 #교환횟수 + 1
  for k in range(j, m2):
    B.append(A[k])
    # Ms += 1 #교환횟수 + 1
  for k in range(r, last):
    B.append(A[k])
    # Ms += 1 #교환횟수 + 1
  
  for i in range(first, last): # B에 있는 값(정렬된 A)를 A로 이동
    A[i] = B[i - first]


A = [40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29,40, 39, 38 , 37, 36, 35, 34, 33 ,32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 , 1]

n = len(A)
print(n)
# random.seed()

# for i in range(n):
#     A.append(random.randint(-1000,1000))

print(A)
three_merge_sort(A, 0, n)
print(A)