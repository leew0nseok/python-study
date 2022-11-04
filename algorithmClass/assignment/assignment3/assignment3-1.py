#제출코드
def binary_search(A, first, last):
  if first > last: return 0
  m = (first + last) // 2
  if A[m-1] > A[m]: # m인덱스 있는 값 왼쪽 값과 비교, 왼쪽 값이 큰 경우 rotate 지점
    return m
  elif A[m] > A[0]: # A[m]이 리스트의 첫번째 원소보다 클 경우 중간부터 끝까지 재귀호출
    return binary_search(A, m+1, last)
  elif A[m] < A[last -1]: # A[m]이 리스트의 마지막 원소보다 작을 경우 처음부터 중간까지 재귀호출
    return binary_search(A, first, m-1)

cnt = 0
A = list(map(int, input().split()))
n = len(A)
idx = binary_search(A, 0, n-1) #정렬되지 않은구간 -> 정렬구간으로 바뀐 인덱스값
if A[0] < A[n-1]: #rotation이 전혀 이뤄지지 않은 리스트
  cnt = 0
else:
  cnt = n - idx

print(cnt)
"""
위의 함수 binary_search()는 A의 중간에 위치한 값(A[m])과 그 앞의 원소(A[m-1])를 비교하여 A[m-1]의 값이 클 경우 m값을 리턴하는 함수이다.
크지 않을경우 반으로 나눠 재귀호출로 탐색하게된다. 여기서 elif A[m] > A[0] 와 elif A[m] < A[last -1]: 조건문 중 성립하는 하나만 재귀호출 하므로 
binary_search()의 시간을 T(n)이라고 하면 T(n) = T(2/n) + c로 나타낼 수 있다. 점화식을 풀면 O(logn)이다. 
위 코드를 이용하면 O(logn)시간에 rotate한 횟수를 구할 수 있다.
위 코드의 경우 비교횟수는 최선의 경우는 리스트의 중간에 위치한 값이 바로 전 값보다 작을 경우 한번에 찾는경우 이므로 1이다.
최악의 경우 비교횟수는 반으로 나누어 탐색하므로 logn+1이며 이것은 다시 O(logn)으로 나타낼 수 있다.
"""


"""
#merge_sort를 변형하여 횟수 찾기
def binary_search(A, first, last):
  if first >= last: return
  binary_search(A, first, (first+last)//2) #앞부분 재귀 정렬
  binary_search(A, (first+last)//2+1, last) #뒷부분 재귀 정렬
  check_not_sort(A, first, last) #정렬된 두 부분 합병

def check_not_sort(A, first, last):
  global cnt
  m = (first + last) // 2
  i, j = first, m+1
  while i <= m and j <= last:
    if A[i] <= A[j]: #A[i]가 더 작을경우 B에 A[i] append
      i += 1
    else: #A[j]가 A[i]보다 더 작을 경우, 이 경우가 리스트의 왼쪽 값이 오른쪽 값보다 큰 경우(rotate된 자리)
      cnt += 1 + (last - j) #else의 경우 A[i]>A[j]인 경우이다. 따라서 횟수 1회와 나머지 A[j]의 오른쪽에 있는 갯수를 더해주면 rotate 횟수
      return
      j += 1

cnt = 0
A = list(map(int, input().split()))
n = len(A)
binary_search(A, 0, n-1)
print(cnt)
위 코드는 merge_sort방식을 활용하여 작성한 코드이다. 
check_not_sort함수에서 cnt변수를 넣어 rotate 횟수를 구하였다. 
분할정복을 통해 binary_search()함수에서 앞, 뒤로 2부분으로 나누면서서 A[i]와 A[j]의 값을 비교했다.
비교시, A[i]값이 A[j]보다 큰 경우 rotate 된 경우이다.
따라서 cnt에 1회를 더해주고 나머지 A[j]의 오른쪽은 정렬되있으므로 같이 rotate된 경우이므로 + last - j 를 해주었다.
위 코드의 수행시간은 binary_search함수는 이진탐색과 같이 두 부분으로 나눠 수행하므로 T(2/n)을 두번 수행한다.
check_not_sort함수는 n의 반까지 확인하기 때문에 2/n시간이 소요된다.
따라서 총 코드의 수행시간 T(n) = 2T(2/n) + cn = O(nlogn)이다.
"""

##############################################

"""
#처음 제출한 코드(수정해야할 것 같음)
def searchIndex(A, first, last):
  m = (first+last)//2
  if A[m-1] > A[m]: #index이므로 -1
    return A[m] #리스트에서 정렬되지 않은 부분의 마지막 원소를 반환
  if sorted(A[:m-1]) == A[:m-1]: #한쪽이 정렬이면 다른 한쪽만 재귀하면 됨. python의 정렬 알고리즘 O(nlogn)
    return searchIndex(A, m, last)
  else:
    return searchIndex(A, 0, m-1)


A = list(map(int, input().split()))
n = len(A)
if sorted(A) == A: #A가 정렬되있으면 0 리턴
  cnt = 0
else: #정렬되지 않을경우 인덱스 리턴
  cnt = len(A) - A.index(searchIndex(A, 0, n))
#print(searchIndex(A, 0, n))
print(cnt)
"""