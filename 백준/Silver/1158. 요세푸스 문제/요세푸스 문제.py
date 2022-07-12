n, k = map(int, input().split())
people = []
for i in range(n):
    people.append(i+1)

queue = []
i = 0
for _ in range(n):
    i += k-1
    if i >= len(people):
        i = i % len(people)
    queue.append(str(people.pop(i)))

print("<", ", ".join(queue)[:], ">", sep='')

# print('<', end='')
# for x in range(len(queue)):
#     if x+1 == len(queue):
#         print(queue[x], end='')
#     else:
#         print(queue[x], end=', ')
# print('>', end='')