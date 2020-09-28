def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?: "))

for el in fact(n):
    print(el)
