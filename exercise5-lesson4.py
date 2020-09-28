from functools import reduce

exersice_list = [n for n in range(100, 1001) if n % 2 == 0]

print(reduce(lambda a, b: a * b, exersice_list))
