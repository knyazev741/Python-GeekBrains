result = {}

with open("ex6.txt", encoding="utf8") as file:
    for item in file.readlines():
        all_hours = []
        for i in item.split():

            if "—" in i:
                pass
            elif "(" in i:
                all_hours.append(int(i[:i.index("(")]))
            else:
                c = i

            summ = 0

            for n in all_hours:
                summ += n

            result.update({c[:-1]: summ})

print(result)
