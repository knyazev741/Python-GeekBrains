a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

def sum(one, two, three):
    if one > two and one > three:
        if two > three or two == three:
            return one + two
        else:
            return one + three
    elif one > two and one < three:
        return one + three
    elif one < two and one < three:
        return two + three
    else:
        return one + two

print(sum(a, b, c))
