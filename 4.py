
exercise_list = [i for i in input("Введите слова через пробел: ").split()]

count = 1
for word in exercise_list:
    if len(word) <= 10:
        print(count, word)
    else:
        print(count, word[0:10])
    count += 1
