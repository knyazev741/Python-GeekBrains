with open("income.txt", "r") as file:
    content = file.readlines()
    personal = {}

    for item in content:
        personal.update({item.split()[0]: int(item.split()[1])})

    for profit in personal.items():
        if profit[-1] < 20000:
            print(profit[0], profit[-1])

    summ = 0

    for income in personal.values():
        summ += income
    print("Средний доход сотрудников равен", summ / len(personal))
