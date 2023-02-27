# 0/1 Knapsack문제

# 0/1 knapsack함수
def knapsack(i, size):
  global MP
  P, S = 0, 0
  if i >= n or size <= 0: #바닥조건
    return
  for j in range(i): #s(v), p(v) 계산
    if x[j] == 1:
      S += s[j]
      P += p[j]
  #x[i] = 1인 경우 시도
  if s[i] <= size:
    B = fractional(i+1, size - s[i])
    if MP < (P + p[i] + B):
      if MP < P + p[i]: #Update MP
        MP = P + p[i]
      x[i] = 1
      knapsack(i+1, size - s[i])
  #x[i] = 0인 경우 시도
  B = fractional(i+1, size)
  if MP < P + B:
    x[i] = 0
    knapsack(i+1, size)

# 한계함수(fractional knapsack)
# 1. size조건
# 2. 예상이익 > MP일 경우 내려간다.
def fractional(i, size):
  P, S = 0, 0
  if size <= 0: #바닥조건
    return 0
  for j in range(i, n):
    if S + s[j] <= size:
      P += p[j]
      S += s[j]
    else:
      P += value[j] * (size-S)
      S = size
      break
    
  return P
  
k = int(input()) #배낭 크기
n = int(input()) #아이템 갯수
s = list(map(int, input().split())) #아이템 크기
p = list(map(int, input().split())) #아이템 가치
x = [0] * n
MP = 0
value = [0] * n #가성비
for i in range(n):
  value[i] = p[i]/s[i] #//으로 할 경우 6번 케이스 통과x
# value.sort(reverse=True) #가성비 큰 순서대로 정렬
for i in range(n): # 가성비 큰 순으로 정렬하면서 s와 p의 리스트도 value의 인덱스에 맞게 정렬
  for j in range(i+1, n):
    if value[i] < value[j]:
      value[i], value[j] = value[j], value[i]
      s[i], s[j] = s[j], s[i]
      p[i], p[j] = p[j], p[i]

knapsack(0, k)
print(MP)