from itertools import cycle

a = ['g', 'e', 'e', 'k', 'b', 'r', 'a', 'i', 'n', 's']

c = 1

for n in cycle(a):
    if c > len(a):
        break
    else:
        print(n)
        c += 1
