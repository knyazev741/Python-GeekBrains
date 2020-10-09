import json

with open("ex7.txt", "r") as file:
    firms_profit = {}
    middle_profit = {}

    for item in file:
        profit = int(item.split()[-2]) - int(item.split()[-1])
        firms_profit.update({item.split()[0]: profit})

    count = 0
    total_profit = 0

    for i in firms_profit.values():
        count += 1
        if i > 0:
            total_profit += i
        else:
            pass

    middle_profit.update({"average_profit": total_profit // count})

    result = [firms_profit, middle_profit]

print(result)

with open("result.json", "x") as file:
    json.dump(result, file)
