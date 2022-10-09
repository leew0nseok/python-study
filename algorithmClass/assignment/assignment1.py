import time, random
from datetime import timedelta
import matplotlib.pyplot as plt

def compute_e_ver1(n):
	# code for O(n^2)-time version
	num = 0
	for i in range(1, n+1):
		bunmo = 1
		for j in range(1, i + 1):
			bunmo *= j
		num += 1/bunmo
	# print('ver1 오일러의 수: ', num)
	
def compute_e_ver2(n):
	# code for O(n)-time version
	fact = 1
	num = 0
	for i in range(1, n+1):
		fact *= i
		num += 1/fact
	# print('ver2 오일러의 수: ', num)
	
def time_NN(A, B, n):
    sum = 0
    for i in range(n):
        for j in range(i):
          sum = sum + A[j]*B[j]
            

def time_N(n):
    a = 1
    for i in range(n):
        a *= i

time_ver1 = []
time_ver2 = []
time_n = []
time_nn = []

# n 입력받음
# n = int(input())
# compute_e_ver1 호출
# before1 = time.process_time()
# compute_e_ver1(n)
# after1 = time.process_time()
# # compute_e_ver2 호출
# before2 = time.process_time()
# compute_e_ver2(n)
# after2 = time.process_time()


x = [1, 10, 50, 100, 200, 300, 400, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
# x = [1, 10, 50, 100, 200, 300, 400, 500, 1000]

for n in x:
	# before1 = time.process_time()
	# compute_e_ver1(n)
	# after1 = time.process_time()
	# time_ver1.append(after1 - before1)

	# before2 = time.process_time()
	# compute_e_ver2(n)
	# after2 = time.process_time()
	# time_ver2.append(after2 - before2)

	before3 = time.process_time()
	time_N(n)
	after3 = time.process_time()
	time_n.append(after3 - before3)

	arrA = [random.randint(0, 999) for _ in range(n)]
	arrB = [random.randint(0, 999) for _ in range(n)]
	before4 = time.process_time()
	time_NN(arrA, arrB, n)
	after4 = time.process_time()
	time_nn.append(after4 - before4)
	




# before3 = time.process_time()
# time_NN(n)
# after3 = time.process_time()

# before4 = time.process_time()
# time_N(n)
# after4 = time.process_time()

# 두 함수의 수행시간 출력
# print("ver1 시간: " , after1 - before1)
# # print("ver1 시간: ", timedelta(seconds=after1 - before1))
# print("ver2 시간: " , after2 - before2)
# print("ver2 시간: ", timedelta(seconds=after2 - before2))
print("n 시간: " , after3 - before3)
# print("n제곱 시간: ", timedelta(seconds=after3 - before3))
print("n제곱 시간: " , after4 - before4)
# print("n 시간: ", timedelta(seconds=after4 - before4))

# plt.plot(x, time_ver1, label='ver1')
# plt.plot(x, time_ver2, label='ver2')
plt.plot(x, time_n, label='O(n)')
plt.plot(x, time_nn, label='O(n^2)')
plt.title('Running Time Analysis')

plt.xlabel('n')
plt.ylabel('time')
plt.legend(loc='upper right')

# plt.xscale("log")
# plt.yscale("log")

plt.show()