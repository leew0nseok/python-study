#동전 0
n, k = map(int, input().split())

arr =[]

for i in range(n):
  arr.insert(0, int(input()))
  
count = 0
j = 0
while k > 0:
  if arr[j] <= k:
    count += k // arr[j]
    k %= arr[j]
  j +=1
    
print(count)