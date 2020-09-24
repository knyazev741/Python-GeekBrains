a = []

while True:
    b = [i for i in input("Введите числа через пробел. Для завршения программы введите символ ! ").split()]
    for item in b:
        if item == "!":
            sum = 0
            for number in a:
                sum = sum + int(number)
            print(sum)
            break
        else:
            a.append(item)
    if item == "!":
        break
    else:
        sum1 = 0
        for number1 in a:
            sum1 = sum1 + int(number1)
        print(sum1)
