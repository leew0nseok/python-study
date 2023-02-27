#O(nlogn)
n = int(input())
datas = []
for i in range(n): #O(n)
	datas.append(list(map(int, input().split())))

arr = [0] * (2*n) #2*n크기의 리스트 생성

for i in range(n): #O(n)
  arr[i] = (datas[i][0], 1) #시작지점, 1
  arr[i+n] = (datas[i][1], -1) #끝나는점, -1

arr.sort(key=lambda x:x[0]) #O(nlogn) #튜플에서 인덱스 0을 기준으로 오름차순 정렬, 같을 경우 시작지점이 끝나는점보다 먼저오게됨.
count = 0 
countlist = [] #가장 먼저오는 시작점부터 늦게끝나는 점까지 못이 통과한 막대갯수를 저장한 리스트

for i in arr: #O(n)
  count += i[1]
  countlist.append(count)

print(max(countlist)) #통과한 막대의 개수

'''
위 코드의 수행시간은 for문 3번으로 3n번의 시간과 파이썬의 내장함수인 sort를 이용하여 nlogn의 수행시간이 소요된다.
따라서 총 수행시간은 O(nlogn)으로 나타낼 수 있다.
n개의 막대를 입력받은 후 datas에 저장한다. datas에는 시작점, 끝나는점을 리스트로 저장했다면,
arr에는 (시작점 인덱스, 1)와 (끝나는점 인덱스, -1)로 저장하였다. 
sort함수를 이용하여 시작점과 끝나는점을 비교하여 오름차순으로 정렬하였고 같을 경우 시작점이 먼저와 +1을 해줄 수 있도록 하였다.
(못이 막대의 끝을 통과하더라도 꽂은 것으로 간주하기 때문)
for문을 통해 arr에서 1과 -1이 있는 부분을 cnt에 저장하며 통과한 막대의 개수를 저장하고 각 통과한 개수를 countlist에 넣어주었다.
+1일 경우 막대의 시작점이며 -1일경우 막대가 끝나는 부분이다.
countlist에서의 최대값이 못 하나로 관통할 수 있는 막대의 최대 개수이다.
'''