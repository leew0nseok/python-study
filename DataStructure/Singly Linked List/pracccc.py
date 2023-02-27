def sort(data, n):
    for x in range(1, n):
        elem = data[x]
        y = x
        while y > 0 and data[y-1] < elem:
            data[y] = data[y-1]
            y = y-1
        data[y] = elem
    return data


print(sort([4, 1, 2, 3, 5], 3))
