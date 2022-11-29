W = int(input())
words = input().split()
# # code below

n = len(words)
wordslen =[] #단어길이 리스트
dptable = [[10000001]*n for i in range(n)] #단어 길이를 넣은 테이블
penaltytable1 = [[10000001]*n for i in range(n)] #패널티 테이블
penaltytable2 = [[10000001]*n for i in range(n)] #각 줄의 패널티 합 테이블
space = 0 #공백

for i in range(n): #wordslen에 단어길이를 넣어줌  
  wordslen.append(len(words[i]))

for i in range(n): #dptable[i][i]를 wordslen[i]로 설정
  dptable[i][i] = wordslen[i]

for i in range(n):
  for j in range(i+1, n):
    if dptable[i][j-1] + wordslen[j] + 1 <= W: #단어길이들의 합과 공백의 길이이 W 보다 작거나 같을 경우 
      dptable[i][j] = dptable[i][j-1] + wordslen[j] + 1 # +1은 공백

# for i in range(n):
#   print(dptable[i])

for i in range(n):
  for j in range(i, n):
    if dptable[i][j] != 10000001:
      penalty = (W-dptable[i][j])**3 
      penaltytable1[i][j] = penalty #penaltytable1에 패널티 채우기

for i in range(n-1, -1, -1):
  penaltytable2[i][i] = penaltytable1[i][n-1]
  # print(penaltytable2)
  for j in range(n-1, -1, -1):
    if penaltytable1[i][j-1] != 10000001:
      if penaltytable2[i][i] > penaltytable2[j][j] + penaltytable1[i][j-1]: #penaltytable2[i][i]의 값이 penaltytable1[i][j-1] + penaltytable2[j][j]보다 클 경우
        penaltytable2[i][i] = penaltytable2[j][j] + penaltytable1[i][j-1]

# for i in range(n):
#   print(penaltytable2[i])
print(penaltytable2[0][0])


'''
우선 입력받은 문자열을 split하여 담은 리스트 words에서 한단어의 길이를 wordslen리스트에 넣는다.
그 후 dptable을 생성하여 인덱스에 맞게 단어의 길이를 dptable에 넣었고, 단어의 합이 폭을 넘어가지 않을 경우 두 단어 길이와 공백길이 합을 넣어주었다.
dptable의 값이 10000001이 아니라면 penaltytable1에 패널티 값을 넣어주었다.
마지막 2중 for문에서 각 패널티가 저장된 penaltytable1에서 패널티를 가져와 
for문을 두번 돌면서 penaltytable1에 있는 값을 가져와 penaltytable2의 값과 합하여 값이 작을경우 penaltytable2에 더 작은 패널티합을 저장하였다.
합이 클 경우 패널티의 합이 큰 경우이므로 penaltytable2에는 더 작은 값을 유지하도록 하였다. 최종적으로 제일 작은 패널티의 합이 penaltytable2[0][0]에 저장된다.
n의 길이만큼 2중 for문을 실행하므로 O(n^2)의 수행시간이 걸린다. 여기서 n은 입력받은 문자열을 split한 갯수로 입력받은 단어의 수이다.
'''