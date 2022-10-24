#merge_sort를 이용하여 횟수 찾기 
def binary_search(A, first, last):
  if first >= last: return
  binary_search(A, first, (first+last)//2) #A의 앞부분 재귀 정렬
  binary_search(A, (first+last)//2+1, last) #A의 뒷 부분 재귀 정렬
  merge_two_sorted_lists(A, first, last) #정렬된 두 부분 합병

def merge_two_sorted_lists(A, first, last):
  global cnt
  m = (first + last) // 2
  i, j = first, m+1
  B = []
  while i <= m and j <= last:
    if A[i] <= A[j]: #A[i]가 더 작을경우 B에 A[i] append
      B.append(A[i])
      i += 1
    else: #A[j]가 A[i]보다 더 작을 경우, 이 경우가 리스트의 왼쪽 값이 오른쪽 값보다 큰 경우(rotate된 자리)
      B.append(A[j])
      cnt += 1 #1회 추가
      cnt += last - j
      return
      j += 1
  #while문을 나왔다는 것은 한쪽 부분의 원소가 다 B에 추가 됬다는 뜻. 따라서 아래 For문 두개중 하나만 실행하여 나머지 원소를 B에 append
  for k in range(i, m+1):
    # cnt += 1 #이동 횟수임.
    B.append(A[k])
  for k in range(j, last+1):
    # cnt += 1 #이동 횟수임.
    B.append(A[k])
  for i in range(first, last+1): # B에 있는 값(정렬된 A)를 A로 이동
    A[i] = B[i - first]
  # return cnt

cnt = 0
A = list(map(int, input().split()))
n = len(A)
binary_search(A, 0, n-1)
print(cnt)