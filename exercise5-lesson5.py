with open("ex5.txt", "x") as file:
    file.write("22 33 44 55 66 77")

with open("ex5.txt", "r") as file:
    all_numbers = file.readline().split()
    summ = 0

    for i in all_numbers:
        summ += int(i)

    print(summ)