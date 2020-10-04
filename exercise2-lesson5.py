with open("second.txt", 'r') as file:
    content = file.readlines()
    count = 0
    for item in content:
        count += 1
        print(f"В строке номер {count} {len(item) - 1} символов")
    print(f"Всего в документе {count} строк")
