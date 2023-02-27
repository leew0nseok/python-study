#숫자 카드 게임
n, m = map(int, input().split())
arr = []

for i in range(n):
  data = list(map(int, input().split()))
  arr.append(data)
  
min_num = 0
for ar in arr:
  if min_num < min(ar):
    min_num = min(ar)

print(min_num)