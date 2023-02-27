# 1904, 01타일
import sys
input = sys.stdin.readline

n = int(input())

DP = [0] * 1000001
DP[1] = 1
DP[2] = 2
for i in range(3, n+1):
  DP[i] = (DP[i-2] + DP[i-1]) %15746 # n이 최대 1,000,000이므로 중간에 int의 범위를 벗어나느 경우가 존재, %15746 추가
  
print(DP[n])