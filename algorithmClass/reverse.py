#비재귀
def reverse(A):
	n, i = len(A), 0
	while i < n//2:
		A[i], A[-1-i] = A[-1-i], A[i]
		i += 1

#재귀
def reverse(L, a):
	n = len(L)
	if a < n//2:
		L[a], L[-a-1] = L[-a-1], L[a]
		reverse(L, a+1)