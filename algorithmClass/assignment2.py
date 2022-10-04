from heapq import heapify, heappush, heappop, nsmallest

#python의 heapq모듈은 기본적으로 최소힙을 제공하므로 최대힙을 만들어줌.
class MaxHeap:
  # 최대 힙 초기화
  def __init__(self):
    self.data = []

  # 최대 힙에 haeppush로 item을 넣어 힙을 유지 O(logn)
  def push(self, item):
    heappush(self.data, -item)

  # 최대 힙에서 루트노드(최대힙이므로 가장큰 값)를 없애고 리턴 O(logn)
  def pop(self):
    return -heappop(self.data)

  def top(self):
    return -self.data[0]
  
  def size(self):
    return len(self.data)


A = list(map(int, input().split()))
# heap = A[:] # heap 변수에 리스트A 복사
# heapify(heap) # 리스트를 힙 자료구조로 변환

num = 0

max_heap = MaxHeap() #최대힙, k번째로 작은 값을 구하기위해 k개의 원소만 존재하도록 유지.
min_heap = [] #최소힙, max_heap의 원소를 k로 유지시키고 리스트A의 원소들을 저장하기위한 힙

for i in range(len(A)): #O(n)
  j = (i//3 + 1) # (i//3 + 1)번째로 작은 값을 정하기 위한 인덱스
  # 최대힙이 비어있거나, 최대힙의 루트값보다 A[i]값이 크거나 같다면, A[i] 삽입
  if max_heap.size() == 0 or max_heap.top() >= A[i]:
    max_heap.push(A[i]) #O(logn)
  # 그 외의 경우, min_heap에 A[i] 삽입
  else:
    heappush(min_heap, A[i]) #O(logn)
  # min_heap의 루트노드(가장 큰 값)을 K번째 작은 수로 만들기 위하여 min_heap의 크기를 k개로 유지
  if max_heap.size() > j:
    heappush(min_heap, max_heap.pop()) #O(logn)
  elif max_heap.size() < j and min_heap:
    max_heap.push(heappop(min_heap)) #O(logn)
    
  num += (max_heap.top() if max_heap.size() >= j else -1) 
  
print(num)

'''
k번째 작은값을 구하기위해 최소힙과 최대힙을 사용하였다.
파이썬의 heapq모듈은 기본적으로 최소힙을 제공하기에 최대힙 Class를 만들어서 보다 쉽게 코드를 작성할 수 있도록 하였다.
k번째 값은 값이므로 최대힙은 k개의 원소를 유지하였고 최대힙에서 pop을 하면 최대힙에 있는 k개의 원소들 중 가장 큰 값이 나오기 때문에 
결과적으론 A[0],...,A[i] 중에서 k번째로 작은 값이다. 
작은 값들을 최대힙에 넣어두고 최대힙의 갯수가 k보다 작으면 최소힙에서 가장 작은 값을 최대힙에 넣어 k개로 맞추고 
k개보다 많다면 최대힙에서 가장 큰 값을 최소힙에 넣어 최대힙, 최소힙을 왔다갔다 하면서 유지하도록 하였다.
처음에는 for문 안에 heapfipy를 사용하여 힙을 만들고 문제를 풀어보았지만 heapfipy자체의 수행시간은 O(nlog)으로 테스트케이스를 통과 못하는 부분이 생겼다.
for문 안에 heapfipy를 쓰니 수행시간은 O(n^2logn)이 였고 시간안에 문제를 해결하려면 for문안에 O(logn)수행시간이 걸리는 코드를 작성해야만 했다.
그렇기에 heappush와 heappop을 이용해 문제를 풀 수 있는 알고리즘을 생각하고 작성했다.
위 코드의 수행시간을 설명하겠다. 수행시간은 기본적으로 for문은 O(n)수행시간이고 안에 있는 heapq모듈의 heappop, heappush는 O(logn) 수행시간이 걸린다. 
상수시간은 무시하므로 전체적으로 O(nlogn)수행시간이 걸린다.
'''


'''
clk = True
i = 0
while clk:
  stack = []
  heappush(heap, A[i])
  heappush(h, A[i])
  # print(h)
  j = (i//3 + 1) # (i//3 + 1)번째로 작은 값을 정하기 위한 인덱스
  
  
  if j == 1:
    continue
  
  if j > 1: # j가 2면 heappop을 한번, j가 3이면 heappop 2번, j가 4면 heappop을 3번...j 가 n이면 heappop을 n-1번 해야함. 반복안하고 how?
    stack.append(heappop(h))
    print("스택 = ", stack)
  print("h0은",h[0])
  num += h[0]
  if j > 1:
    heappush(h, stack.pop())
  i += 1 # i 인덱스 1씩 증가
  if i > len(A): #반복문 종료
    clk = False
  
print(num)'''


'''
#지금까지 푼 코드 중 가장 빠른 코드
for i in range(len(A)): #(On) * O(n)
	m = A[:i + 1] # 리스트 슬라이싱을 이용해 새로운 리스트m을 만듬
	heapify(m) # O(n)
	j = (i//3 + 1) # (i//3 + 1)번째로 작은 값을 정하기 위한 인덱스
	if j > 1:
		for _ in range(0, j-1):
			heappop(m)
	num += m[0]
	
print(num)'''
	
	
'''
문제해석
입력 : 9 1 3 2 7 0 -2 4 5
m[0] = 9 [9] 1번째 작은 값 = 9
m[1] = 1 [1, 9] 1번째 값은 값 = 1
m[2] = 1 [1, 3, 9] 1번째 작은 값 = 1
m[3] = 2 [1, 2, 3, 9] 2번째 작은 값 = 2
m[4] = 2 [1, 2, 3, 7, 9] 2번째 작은 값 = 2
m[5] = 1 [0, 1, 2, 3, 7, 9] 2번째 작은 값 = 1
m[6] = 1 [-2, 0, 1, 2, 3, 7, 9] 3번째 작은 값 = 1
m[7] = 1 [-2, 0, 1, 2, 3, 4, 7, 9] 3번째 작은 값 = 1
m[8] = 1 [-2, 0, 1, 2, 3, 4, 5, 7, 9] 3번째 작은 값 = 1
출력 : 19
'''