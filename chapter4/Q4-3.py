n = str(input())

startx = 0
starty = 0

startx += int(ord(n[0])) - int(ord('a')) + 1
starty += int(n[1])
  
print(startx, starty)
route = [(-1, 2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2, -1)]

cnt = 0

for r in route:
  finshx = startx + r[0]
  finshy = starty + r[1]
  
  if finshx > 8 or finshx <= 0 or finshy <= 0 or finshy > 8:
    continue
  else:
    cnt += 1
    
print(cnt)