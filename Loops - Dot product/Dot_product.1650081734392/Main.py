# Dot product
# write the dot_product function here
def dot_product(a, b):
    dot = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
    return dot


a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
dot = dot_product(a, b)
print(dot)
