n = int(input())
datas = []
for i in range(n): #O(n)
	datas.append(list(map(int, input().split())))

datas.sort(key=lambda x:x[1]) #O(nlogn), 1번 인덱스 기준으로 정렬

L, selected = [0] , 0
for i in range(1, n): #O(n)
  if datas[selected][1] < datas[i][0]:
    L.append(i)
    selected = i

print(len(L))
'''
입력받은 n개의 막대 데이터를 끝나는 점을 기준으로 오름차순 정렬을 해준다. lambda를 이용하여 끝점기준으로 오름차순 정렬을 해주었고 이 때 O(nlogn)의 수행시간이 소요된다.
처음으로 가장 빨리 끝나는 막대는 못이 필요하기때문에 L에 datas의 첫 막대 인덱스인 0을 넣어주었고 selected란 변수를 선언해 인덱스 값0을 설정해주었다.
그 후 for문을 통해 selected번째 막대의 끝점과 i번째 막대의 시작점을 비교하면서 i번째 막대의 시작점이 selected번째 막대보다 클 경우 겹치지 않는 경우로 새로운 못이 필요하다.
따라서 새로운 못이 필요한 지점의 값을 사진 datas 인덱스를 L에 넣어준다. 그럼 이 시작점으로부터 시작한 막대의 끝점과 또 다음 막대의 시작점을 비교하여 다음 막대의 시작점의 값을 가진 datas의 인덱스를 L에 넣어준다.
for문 종료 후 L에 저장된 값들은 못들이 필요한 지점이므로 L의 갯수는 최소한으로 필요한 못의 개수이다.
길이가 n인 for문 두번과 sort정렬을 하므로 위 코드의 총 수행시간은 O(nlogn)이다.
'''