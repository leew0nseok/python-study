#게임 개발
n, m = map(int, input().split()) #n * m 맵 생성
x, y, d = map(int, input().split()) #(x, y)에 d를 바라보고 있는 캐릭터

#방문한 위치를 저장하기 위한 맵
check = [[0] * m for _ in range(n)]
check[x][y] = 1
data = []

for i in range(n):
  data.append(list(map(int, input().split())))
  
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -=1
  if d == -1:
    d = 3
    

count = 1
turn_time = 0

while True:
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]
  
  if check[nx][ny] == 0 and data[nx][ny] == 0:
    check[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time +=1
  if turn_time == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    if data[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0
    
print(count)
  


