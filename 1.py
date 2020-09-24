x = int(input("Введите делимое число: "))
y = int(input("Введите делитель: "))

def share(divident, divider):
    if divider == 0:
        return "На ноль делить нельзя"
    else:
        return divident / divider

print(share(x, y))
