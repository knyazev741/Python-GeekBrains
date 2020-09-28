question = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([question[i] for i in range(len(question)) if question[i] not in question[i + 1:] and question[i] not in question[:i]])
