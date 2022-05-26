# Sorting-Compare(Lab)
import random
import time

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
        return

    mid = len(S) // 2
    S1 = S[0: mid]
    S2 = S[mid: len(S)]

    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)


def quick_sort(S):
    # base case for Recur
    if len(S) < 2:
        return

    # devide
    pivot = S[0]
    L, E, G = [], [], []
    while len(S) > 0:
        x = S.pop()
        if x < pivot:
            L.append(x)
        elif x == pivot:
            E.append(x)
        else:
            G.append(x)

    quick_sort(L)
    quick_sort(G)

    # #combine L, E, G to S
    # for i in range(len(L)):
    # 	S.append(L[i])
    # for z in range(len(E)):
    # 	S.append(E[z])
    # for j in range(len(G)):
    # 	S.append(G[j])

    while len(L) > 0:
        S.append(L.pop(0))
    while len(E) > 0:
        S.append(E.pop(0))
    while len(G) > 0:
        S.append(G.pop(0))


n = 100  # change this value to compare different algorithms	#배열의 길이
array = [random.randint(0, 999999999) for _ in range(n)]

array_insertion = array.copy()
start = time.perf_counter()
insertion_sort(array_insertion)
t_insertion = time.perf_counter() - start

array_merge = array.copy()
start = time.perf_counter()
merge_sort(array_merge)
t_merge = time.perf_counter() - start

array_quick = array.copy()
start = time.perf_counter()
quick_sort(array_quick)
t_quick = time.perf_counter() - start

if not is_sorted(array_insertion):
    print("insertion_sort: incorrect")
else:
    print("insertion_sort running time:", t_insertion)

if not is_sorted(array_merge):
    print("merge_sort:     incorrect")
else:
    print("merge_sort running time:", t_merge)

if not is_sorted(array_quick):
    print("quick_sort:     incorrect")
else:
    print("quick_sort running time:", t_quick)
