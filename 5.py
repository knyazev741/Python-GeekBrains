#Не нашел решение

rating = [10, 9, 5, 5, 2, 1]

new_number = int(input("Введите новый номер в рейтинге: "))
count = 0

for number in rating:
    if new_number > number:
        rating.insert(count, new_number)
        break
    elif new_number == number:
        if count == rating[-1]:
            rating.append(new_number)
        else:
            rating.insert(count + 1, new_number)
    else:
        count += 1

print(rating)
