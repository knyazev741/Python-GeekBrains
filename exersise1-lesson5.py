with open("text.txt", "x") as file:
    while True:
        content = input("Введите информацию для записи: ")
        if bool(content) is False:
            break
        else:
            file.write(content + "\n")

