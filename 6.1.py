def int_func(word):
    first = []
    for i in range(len(word)):
        if i == 0:
            first.append(word[0].upper())
        else:
            first.append(word[i])
    return ''.join(first)

a = [y for y in input("Введите слова с маленькой буквы через пробел: ").split()]

res = []

for item in a:
    res.append(int_func(item))

print(' '.join(res))
