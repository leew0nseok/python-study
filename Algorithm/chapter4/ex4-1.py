#상하좌우

n = int(input())
r = list(map(str, input().split()))

start = [1, 1]

for m in r:
  if m == "R":
    if start[1] == n:
      continue
    start[1] += 1
  elif m == "L":
    if start[1] == 1:
      continue
    start[1] -= 1
  elif m == "U":
    if start[0] == 1:
      continue
    start[0] -= 1
  elif m == "D":
    if start[0] == n:
      continue
    start[0] += 1

print(start[0], start[1])

'''
#교재 코드
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인
for plan in plans:
  #이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  #공간을 벗어나느 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  #이동수행
  x, y = nx, ny
  
print(x,y)
'''