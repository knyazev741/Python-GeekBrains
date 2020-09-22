test_list = input("Введите что нибудь: ")

max_index = len(test_list)
start = 0

prod_list = []

if max_index % 2 == 0:
    while start <= max - 2:
        prod_list.insert(start, test_list[start + 1])
        prod_list.insert(start + 1, test_list[start])
        start = start + 2
else:
    while start <= max - 2:
        prod_list.insert(start, test_list[start + 1])
        prod_list.insert(start + 1, test_list[start])
        start = start + 2
    prod_list.append(test_list[-1])

print(prod_list)
