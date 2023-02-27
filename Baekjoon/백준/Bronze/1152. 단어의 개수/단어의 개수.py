import re

a = input()
val = len(re.findall(r'\w+', a))

print(val)
