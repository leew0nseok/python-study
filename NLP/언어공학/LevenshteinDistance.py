# str1 = "intention"
# str2 = "execution"
str1 = input()
str2 = input()
cost = 2

str1 = str1.split()
str2 = str2.split()
n = len(str1)+1
m = len(str2)+1

matrix = [[0]*n
          for _ in range(m)]
for i in range(n):
  matrix[0][i] = i
for j in range(m):
  matrix[j][0] = j

for i in range(1,m):
  for j in range(1,n):
    if str1[j-1] == str2[i-1]:
      matrix[i][j] = matrix[i-1][j-1]
    else:
      a = matrix[i][j-1]+1
      b = matrix[i-1][j]+1
      c = matrix[i-1][j-1]+cost
      min_num = min(a,b,c)
      matrix[i][j] = min_num


for i in range(m):
  for j in range(n):
    print(matrix[i][j], end=" ")
  print()
print(matrix[-1][-1])