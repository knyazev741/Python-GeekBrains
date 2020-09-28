test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [test_list[i + 1] for i in range(len(test_list) - 1) if test_list[i + 1] > test_list[i]]

print(new_list)
