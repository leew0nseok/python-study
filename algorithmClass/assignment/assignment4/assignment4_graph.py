import random, timeit
import matplotlib.pyplot as plt
import numpy as np

#quick_sort
def quick_sort(A, first, last):
  global Qc, Qs
  if first >= last: return
  left, right = first+1, last
  pivot = A[first]
  while left <= right:
    while left <= last and A[left] < pivot:
      Qc += 1 #비교횟수 + 1
      left += 1
    while right > first and A[right] > pivot:
      Qc += 1 #비교횟수 + 1
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

#수행시간 저장 리스트
timeQs = []
timeQsi = []
timeMs = []
timeTMs = []
timeHs = []
#교환횟수 저장 리스트
countswapQs = []
countswapQsi = []
countswapMs = []
countswapTMs = []
countswapHs = []
#비교횟수 저장 리스트
countcompareQs = []
countcompareQsi = []
countcompareMs = []
countcompareTMs = []
countcompareHs = []
#비교+교환횟수 저장 리스트
countswapcompareQs = []
countswapcompareQsi = []
countswapcompareMs = []
countswapcompareTMs = []
countswapcompareHs = []

p = [1, 10, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]

for k in p:
  random.seed()
  data = []
  for i in range(k):
    data.append(random.randint(-1000,1000))
  A = data[:]
  B = data[:]
  C = data[:]
  D = data[:]
  E = data[:]
  n = len(data)
  
  quick_sort(A, 0, n-1)
  quick_sort_insertion(D, 0, n-1)
  merge_sort(B, 0, n-1)
  three_merge_sort(E, 0, n)
  heap_sort(C)
  
  #교환횟수 비교
  countswapQs.append(Qs)
  countswapQsi.append(Qsi)
  countswapMs.append(Ms)
  countswapTMs.append(Ms3)
  countswapHs.append(Hs)
  
  
  """
  #비교횟수 비교
  countcompareQs.append(Qc)
  countcompareQsi.append(Qci)
  countcompareMs.append(Mc)
  countcompareTMs.append(Mc3)
  countcompareHs.append(Hc)
  plt.plot(p, countcompareQs, color = "black", label='quick_sort')
  plt.plot(p, countcompareQsi, color = "purple", label='quick_sort_insertion')
  plt.plot(p, countcompareMs, color = "yellow", label='merge_sort')
  plt.plot(p, countcompareTMs, color = "green", label='three_merge_sort')
  plt.plot(p, countcompareHs, color = "red", label='heap_sort')
  plt.title('Compare')
  """  
  """
  #교환+비교횟수 비교
  countswapcompareQs.append(Qs + Qc)
  countswapcompareQsi.append(Qsi + Qci)
  countswapcompareMs.append(Ms + Mc)
  countswapcompareTMs.append(Ms3 + Mc3)
  countswapcompareHs.append(Hs + Hc)
  plt.plot(p, countswapcompareQs, color = "black", label='quick_sort')
  plt.plot(p, countswapcompareQsi, color = "purple", label='quick_sort_insertion')
  plt.plot(p, countswapcompareMs, color = "yellow", label='merge_sort')
  plt.plot(p, countswapcompareTMs, color = "green", label='three_merge_sort')
  plt.plot(p, countswapcompareHs, color = "red", label='heap_sort')
  plt.title('Swap + compare')
  """
  """
  #수행시간 비교
  timeQs.append(timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
  timeQsi.append(timeit.timeit("quick_sort_insertion(D, 0, n-1)", globals=globals(), number=1))
  timeMs.append(timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
  timeTMs.append(timeit.timeit("three_merge_sort(E, 0, n)", globals=globals(), number=1))
  timeHs.append(timeit.timeit("heap_sort(C)", globals=globals(), number=1))
  plt.plot(p, timeQs, color = "black", label='quick_sort')
  plt.plot(p, timeQsi, color = "purple", label='quick_sort_insertion')
  plt.plot(p, timeMs, color = "yellow", label='merge_sort')
  plt.plot(p, timeTMs, color = "green", label='three_merge_sort')
  plt.plot(p, timeHs, color = "red", label='heap_sort')
  plt.title('Running Time Analysis')
  """

plt.plot(p, countswapQs, color = "black", label='quick_sort')
plt.plot(p, countswapQsi, color = "purple", label='quick_sort_insertion')
plt.plot(p, countswapMs, color = "yellow", label='merge_sort')
plt.plot(p, countswapTMs, color = "green", label='three_merge_sort')
plt.plot(p, countswapHs, color = "red", label='heap_sort')
plt.title('Swap')


plt.xlabel('n')
plt.ylabel('Swap Count')
plt.legend(loc='upper right')



# plt.xscale("log")
# plt.yscale("log")

plt.show()

