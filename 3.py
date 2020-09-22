month = int(input("Введите номер месяца: "))

months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if month in months[0:3]:
    print("Зима")
elif month in months[3:6]:
    print("Весна")
elif month in months[6:9]:
    print("Лета")
else:
    print("Осень")
