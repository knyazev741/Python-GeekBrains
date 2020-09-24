line = input("Введите слово с маленькой буквы: ")

def int_func(word):
    first = []
    for i in range(len(word)):
        if i == 0:
            first.append(word[0].upper())
        else:
            first.append(word[i])
    return ''.join(first)


print(int_func(line))

#Продолжение задачи в файле 6.1