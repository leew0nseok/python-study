#큰 수의 법칙
n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

num= 0
count = 0

for i in range(m):
  if count !=0 and count % k == 0:
    num += arr[1]
  else:
    num += arr[0]
  count += 1
  
print(num)

#교재 코드
'''
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

result = 0

while True:
  for i in range(k): #가장 큰수 k 번 더하기
    if m == 0: #m이 0이면 탈출
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1
  
print(result)'''
