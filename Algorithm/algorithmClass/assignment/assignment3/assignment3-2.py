def find_k(arr, first1, first2, last1, last2, k):
  global clk
  global idx, idy
  if first1 > last1 or first2 > last2: return #인덱스 범위 초과
  m1 = (first1 + last1) // 2
  m2 = (first2 + last2) // 2
  if (m2+1 > first2 and m2+1 > last2): return
  if first1 +1 == last1 and first2 +1 == last2:
    x = arr[last1][first2]
    y = x
    v = True
  else:
    x = arr[m1][m2]
    y = arr[m1+1][m2+1]
  print("x, y, [m1][m2]", x, y, m1, m2, m1+1, m2+1, k)
  if clk == False:
    if x == k:
      clk, idx, idy = True, m1, m2
      return
    elif y == k:
      clk = True
      clk, idx, idy = True, m1+1, m2+1
      return
    elif x > k:
      print("x > k")
      find_k(arr, first1, m2+1, m1, last2, k) #1사분면
      find_k(arr, first1, first2, m1, m2, k) #2사분면
      find_k(arr, m1+1, first2, last1, m2, k) #3사분면
    elif y < k:
      print("y < k")
      find_k(arr, first1, m2+1, m1, last2, k) #1사분면
      find_k(arr, m1+1, first2, last1, m2, k) #3사분면
      find_k(arr, m1+1, m2+1, last1, last2, k) #4사분면
    elif x < k < y:
      print("x < k < y")
      find_k(arr, first1, m2+1, m1, last2, k) #1사분면 #테스트케이스 1번 통과x
      # find_k(arr, 0, m2+1, m1, last1, k) #1사분면 #테스트케이스 전체통과
      find_k(arr, m1+1, first2, last1, m2, k) #3사분면

n, k = map(int, input().split())
idx, idy = -1, -1
clk = False
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))
  
find_k(arr, 0, 0, n-1, n-1, k)
print("(%d, %d)" %(idx, idy))

'''
위 코드는 4분면으로 이진탐색을 적용하여 코드를 작성하였다. 각 행의 값과 각 열의 값들은 모두 오름차순으로 정렬되어 있기 때문에 이진탐색을 적용할 수 있다.
예를들어 4x4 2차원 리스트에서 k=16을 찾으려면 arr[1][1] = 8과 arr[2][2] = 20을 비교하여 8<k<20이므로 k는 1,3 분면에 존재하거나 아예 존재하지 않는다. 
따라서 다른 사분면은 볼 필요없이 1, 3분면에 대해서만 재귀호출을 하여 k값의 인덱스를 찾는 방식이다. 위 코드를 점화식으로 나타내면
최악의 경우 T(n) <= 3T(2/n) + c 사분면중 3개를 재귀호출하여 탐색하므로 이런식이 작성된다. 
점화식을 전개할경우 n =2^k라 가정, T(1) = c
T(n) <= 3T(2/n) + c
     <= 3(3T(2/n) + c) + c
     <= 3^3T(2/n) + c(1+ 3+ 3^2)
                  .
                  .
     <= 3^kT(2/n) + c(1+3+······+3^(k-1)) = c3^k = O(3^k) = O(3^(log2의n)) = O(n^(log2의3)) = O(n^(1.5849...))이 된다.
'''

################################################################

"""
#행별로 이진탐색해여 k값 찾기
def binary_search(arr, i, first, last, k):
  if first > last: return 0
  m = (first + last) // 2
  if arr[i][m] == k:
    return i, m
  elif arr[i][m] > k:
    return binary_search(arr, i, first, m-1, k)
  elif arr[i][m] < k:
    return binary_search(arr, i, m+1, last, k)

def find_k(arr, k):
  clk = False
  for i in range(len(arr)): #for문 O(N)
    first, last = 0, len(arr[i])-1
    result = binary_search(arr, i, first, last, k) #이진탐색 O(logn)
    if result != 0:
      return result
  if clk == False:
    return -1, -1

n, k = map(int, input().split())

arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))
  
print(find_k(arr, k))
"""
'''
행마다, 열마다 오름차순으로 정렬된 리스트를 입력받아 행별로 이진탐색을 통해 k값의 인덱스를 리턴하는 코드를 작성하였다.
for문을 통해 n번 돌면서 행을 돌면서 행마다 binary_search를 통해 이진탐색을 진행한다.
행에서 이진탐색을 통해 값이 없을 경우 다음 행으로 넘어가 다시 이진탐색을 진행하고 모든 행을 이진탐색을 통해 탐색했는데 없을 경우 -1, -1을 리턴한다. 
따라서 for문을 도는 n번 동안 행마다 이진탐색을 진행하므로 Big-O는 nlogn이 된다.
binary_search의 수행시간을 T(n)이라고 하면 T(n) = T(2/n) + c 이고 find_k의 수행시간을 F(n)이라고 하면 
F(n) = n*T(n) 이므로 T(n)은 수행시간이 logn이므로 find_k의 수행시간은 nlogn이다.
'''