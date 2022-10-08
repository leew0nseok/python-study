#5430
t = int(input()) #테스트케이스 개수

for i in range(t):
  f = input() #함수
  n = int(input())
  if n == 0:
    arr = []
    input()
  else:
    arr = list(map(int, input()[1:-1].split(',')))
  
  clk = True
  cnt = 0
  
  for j in f:
    if j == "R":
      cnt += 1
    elif j == "D":
      if len(arr) == 0:
        print("error")
        clk = False
        break
      if cnt % 2 == 0: #리버스 안해도 됨.
        arr.pop(0)
      else: #원래는 리버스 한 상태에서 첫 원소니까 리버스 안하고 마지막 원소제거
        arr.pop()  
  
  if clk:
    if cnt % 2 == 1:
      arr.reverse()
    print("[" + ','.join(map(str,arr)) + "]")