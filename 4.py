x = float(input("Введите положительное действительное число: "))
y = int(input("Введите отрицательное целое число: "))

def exponentiation(x, y):
    res = x
    for i in range(1, abs(y)):
        res = res * x
    return 1 / res

print(exponentiation(x, y))

