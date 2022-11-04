import random, timeit

#quick_sort
def quick_sort(A, first, last):
  global Qc, Qs
  if first >= last: return
  left, right = first+1, last
  pivot = A[first]
  while left <= right:
    Qc += 1 #비교횟수 + 1
    while left <= last and A[left] < pivot:
      left += 1
    Qc += 1 #비교횟수 + 1
    while right > first and A[right] > pivot:
      right -= 1
    if left <= right:
      A[left], A[right] = A[right], A[left]
      Qs += 1 #교환횟수 + 1
      left += 1
      right -= 1
  
  A[first], A[right] = A[right], A[first]
  Qs += 1 #교환횟수 + 1
  
  quick_sort(A, first, right-1)
  quick_sort(A, right+1, last)
  
#quick_sort + insertion_sort
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
    Qci += 1
    while left <= last and A[left] < pivot:
      left += 1
    while right > first and A[right] > pivot:
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

#merge_sort
def merge_sort(A, first, last):
  global Mc, Ms
  if first >= last: return
  merge_sort(A, first, (first+last)//2) #A의 앞부분 재귀 정렬
  merge_sort(A, (first+last)//2+1, last) #A의 뒷 부분 재귀 정렬
  merge_two_sorted_lists(A, first, last) #정렬된 두 부분 합병

def merge_two_sorted_lists(A, first, last):
  global Mc, Ms
  m = (first + last) // 2
  i, j = first, m+1
  B = []
  while i <= m and j <= last:
    Mc += 1 #비교 횟수 + 1
    if A[i] <= A[j]: #A[i]가 더 작을경우 B에 A[i] append
      B.append(A[i])
      i += 1
    else: #A[j]가 더 작을 경우 B에 A[j] append
      B.append(A[j])
      j += 1
  #while문을 나왔다는 것은 한쪽 부분의 원소가 다 B에 추가 됬다는 뜻. 따라서 아래 For문 두개중 하나만 실행하여 나머지 원소를 B에 append
  for k in range(i, m+1):
    B.append(A[k])
    Ms += 1 #교환횟수 + 1
  for k in range(j, last+1):
    B.append(A[k])
    Ms += 1 #교환횟수 + 1
  for i in range(first, last+1): # B에 있는 값(정렬된 A)를 A로 이동
    A[i] = B[i - first]
    Ms += 1 #교환횟수 + 1
    
#3way merge_sort
def three_merge_sort(A, first, last):
  global Mc3, Ms3
  if last - first < 2: return
  three_merge_sort(A, first, first + ((last - first) // 3))
  three_merge_sort(A, first + ((last - first) // 3), first + 2 * ((last - first) // 3) + 1)
  three_merge_sort(A, first + 2 * ((last - first) // 3) + 1, last)
  merge_three_sorted_lists(A, first, last)

def merge_three_sorted_lists(A, first, last):
  global Mc3, Ms3
  m1 = first + ((last - first) // 3)
  m2 = first + 2 * ((last - first) // 3) + 1
  i, j, r= first, m1, m2
  B =[]

  while ((i < m1) and (j < m2) and (r < last)):
    Mc3 += 1
    if A[i] < A[j]:
      Mc3 += 1
      if A[i] < A[r]:
        B.append(A[i])
        Ms3 += 1 #교환횟수 + 1
        i += 1
      else:
        B.append(A[r])
        Ms3 += 1 #교환횟수 + 1
        r += 1
    else:
      Mc3 += 1
      if A[j] < A[r]:
        B.append(A[j])
        Ms3 += 1 #교환횟수 + 1
        j += 1
      else:
        B.append(A[r])
        Ms3 += 1 #교환횟수 + 1
        r += 1

  while ((i < m1) and (j < m2)):
    Mc3 += 1
    if A[i] < A[j]:
      B.append(A[i])
      Ms3 += 1 #교환횟수 + 1
      i += 1
    else:
      B.append(A[j])
      Ms3 += 1 #교환횟수 + 1
      j += 1
  while ((j < m2) and (r < last)):
    Mc3 += 1
    if A[j] < A[r]:
      B.append(A[j])
      Ms3 += 1 #교환횟수 + 1
      j += 1
    else:
      B.append(A[r])
      Ms3 += 1 #교환횟수 + 1
      r += 1

  while ((i < m1) and (r < last)):
    Mc3 += 1
    if A[i] < A[r]:
      B.append(A[i])
      Ms3 += 1 #교환횟수 + 1
      i += 1
    else:
      B.append(A[r])
      Ms3 += 1 #교환횟수 + 1
      r += 1

  #while문을 나옴 나머지 원소들 B에 추가.
  for k in range(i, m1):
    B.append(A[k])
    Ms3 += 1 #교환횟수 + 1
  for k in range(j, m2):
    B.append(A[k])
    Ms3 += 1 #교환횟수 + 1
  for k in range(r, last):
    B.append(A[k])
    Ms3 += 1 #교환횟수 + 1
  
  for i in range(first, last): # B에 있는 값(정렬된 A)를 A로 이동
    A[i] = B[i - first]
    Ms3 += 1


#heap sort
def heap_sort(A):
  global Hc, Hs
  n=len(A)
  make_heap(A)
  for k in range(n-1, -1, -1):
    Hs += 1
    A[0],A[k] = A[k],A[0]
    n = n - 1
    heapify_down(A,0,n)

def make_heap(A):
  n=len(A)
  for k in range(n-1,-1,-1):
    heapify_down(A,k,n)

def heapify_down(A,k,n):
  global Hc, Hs
  while 2*k+1 < n:
    L, R = 2*k + 1, 2*k + 2
    Hc += 1
    if L < n and A[L] > A[k]:
      m = L
    else:
      m = k
    Hc += 1
    if R < n and A[R] > A[m]:
      m = R # m = A[k], A[L], A[R] 중 최대값의 인덱스
    if m != k: # A[k]가 최대값이 아니라면 힙 성질 위배
      Hs += 1
      A[k], A[m] = A[m], A[k]
      k = m
    else: 
      break
    



# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

# #
# # Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# # Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# # Qci는 quick sort + insertion에서 리스트의 두 수를 비교한 횟수 저장
# # Qsi는 quick sort + insertion에서 두 수를 교환(swap)한 횟수 저장
# # Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# # Mc3, Ms3는 three_merge sort에서 비교, 교환(또는 이동) 횟수 저장
# # Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
# #

Qc, Qs, Mc, Ms, Hc, Hs, Qci, Qsi, Mc3, Ms3  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("")
print("Quick sort + insertion sort:")
print("time =", timeit.timeit("quick_sort_insertion(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qci, Qsi))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
print("three_Merge sort:")
print("time =", timeit.timeit("three_merge_sort(E, 0, n)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc3, Ms3))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))