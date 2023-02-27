import random
import time
import matplotlib.pyplot as plt
import numpy as np

"""To check if the array is sorted"""


def is_sorted(A):
    if len(A) < 2:
        return True

    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False

    return True


"""sorting algorithms"""


def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


def merge_sort(S):
    if len(S) < 2:
        return S

    mid = len(S) // 2
    S1 = S[0: mid]
    S2 = S[mid: len(S)]

    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)
    pass


def quick_sort(S):
    if len(S) <= 1:
        return S
    pivot = S[0]
    L, E, G = [], [], []
    for num in S:
        if num < pivot:
            L.append(num)
        elif num > pivot:
            G.append(num)
        else:
            E.append(num)
    return quick_sort(L) + E + quick_sort(G)


# def quick_sort(S):
#     # base case for Recur
#     if len(S) < 2:
#         return

#     # devide
#     pivot = S[0]
#     L, E, G = [], [], []
#     while len(S) > 0:
#         x = S.pop()
#         if x < pivot:
#             L.append(x)
#         elif x == pivot:
#             E.append(x)
#         else:
#             G.append(x)

#     quick_sort(L)
#     quick_sort(G)

#     # #combine L, E, G to S
#     # for i in range(len(L)):
#     # 	S.append(L[i])
#     # for z in range(len(E)):
#     # 	S.append(E[z])
#     # for j in range(len(G)):
#     # 	S.append(G[j])

#     while len(L) > 0:
#         S.append(L.pop(0))
#     while len(E) > 0:
#         S.append(E.pop(0))
#     while len(G) > 0:
#         S.append(G.pop(0))

# O(n)시간을 찾기위해 정렬되지 않은리스트에서 최댓값 찾기


def time_N(arr):
    max_value = None

    for num in arr:
        if (max_value is None or num > max_value):
            max_value = num

# 이진탐색을 이용하여 logn시간복잡도 구하기


def time_logN(arr):
    left = 0
    right = len(arr) - 1
    while (right >= left):
        mid = (right + left) // 2

        if(2 == arr[mid]):
            break
        if(2 < arr[mid]):
            right = mid - 1
        else:
            left = mid + 1


def time_NN(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print("")


# n = 100 # change this value to compare different algorithms	#배열의 길이
list_t_insertion = []
list_t_merge = []
list_t_quick = []

timeConstant = []
timelogN = []
timeNlogn = []
timeN = []
timeNN = []

# n의 값에 따른 insertion 시간

k = 1
x = []
while 10001 > k:
    array = [random.randint(0, 999999999) for _ in range(k)]
    array_insertion = array.copy()
    start = time.perf_counter()
    insertion_sort(array_insertion)
    list_t_insertion.append(time.perf_counter() - start)

    # n의 값에 따른 merge 시간
    array = [random.randint(0, 999999999) for _ in range(k)]
    array_merge = array.copy()
    start = time.perf_counter()
    merge_sort(array_merge)
    list_t_merge.append(time.perf_counter() - start)

    # n의 값에 따른 quick 시간
    array = [random.randint(0, 999999999) for _ in range(k)]
    array_quick = array.copy()
    start = time.perf_counter()
    quick_sort(array_quick)
    list_t_quick.append(time.perf_counter() - start)
    x.append(k)

    # O(1)시간 index
    start = time.perf_counter()
    Con = array[0]
    timeConstant.append(time.perf_counter() - start)

    # O(n)시간을 찾기위해 정렬되지 않은리스트에서 최댓값 찾기
    start = time.perf_counter()
    time_N(array)
    timeN.append(time.perf_counter() - start)

    # O(nlogn)시간
    start = time.perf_counter()
    array.sort()
    timeNlogn.append(time.perf_counter() - start)

    # O(logn)
    start = time.perf_counter()
    time_logN(array)
    timelogN.append(time.perf_counter() - start)

    # O(n^2)
    start = time.perf_counter()
    time_NN(array)
    timeNN.append(time.perf_counter() - start)

    k = k * 10


# print(x)

# array_quick = array.copy()
# start = time.perf_counter()
# quick_sort(array_quick)
# t_quick = time.perf_counter() - start


# if not is_sorted(array_insertion):
#     print("insertion_sort: incorrect")
# else:
#     print("insertion_sort running time:", t_insertion)

# if not is_sorted(array_merge):
#     print("merge_sort:     incorrect")
# else:
#     print("merge_sort running time:", t_merge)

# if not is_sorted(array_quick):
#     print("quick_sort:     incorrect")
# else:
#     print("quick_sort running time:", t_quick)


# plt.scatter(ScopeN, list_t_insertion)
plt.plot(x, list_t_insertion, label='insertion')
plt.plot(x, list_t_merge, label='merge')
plt.plot(x, list_t_quick, label='quick')

# plt.plot(x, np.log(x), label='test')

plt.plot(x, timeConstant, label='O(1)')
plt.plot(x, timelogN, label='O(logn)')
plt.plot(x, timeNlogn, label='O(nlogn)')
plt.plot(x, timeN, label='O(n)')
plt.plot(x, timeNN, label='O(n^2)')
plt.title('Running Time Analysis of Sorting')

plt.xlabel('n')
plt.ylabel('insetion time')
plt.legend(loc='upper right')
# plt.xlim([0, 20000])
plt.xscale("log")
plt.yscale("log")

plt.show()
