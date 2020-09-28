from itertools import count

x = int(input("Введите целое число меньше 20: "))

for n in count(x):
    if n > 20:
        break
    else:
        print(n)
