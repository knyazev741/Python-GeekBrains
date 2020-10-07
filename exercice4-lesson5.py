with open("exercise4.txt", "r") as file:
    new_list = []

    for item in file.readlines():
        if "One" in item:
            new_list.append(item.replace("One", "Один"))
        elif "Two" in item:
            new_list.append(item.replace("Two", "Два"))
        elif "Three" in item:
            new_list.append(item.replace("Three", "Три"))
        elif "Four" in item:
            new_list.append(item.replace("Four", "Четыре"))
        else:
            new_list.append(item)

    with open("exercise4-result.txt", "x") as file2:
        for i in new_list:
            file2.write(i)



