# write compute_tsa function here

def compute_tsa(r, h):
	pi = 3.1416
	tsa = 2 * pi * (r**2 + r * h)
	return tsa

r, h = [float(x) for x in input().split()]
pi = 3.1416
tsa = compute_tsa(r,h)
print('%.2f'%(tsa))