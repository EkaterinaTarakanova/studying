sequence = input("Введите последовательность целых чисел")
flag = False
for i in range(len(sequence)):
    if sequence[i] != " ":
        for j in range(i + 1, len(sequence)):
            if sequence[j] != " ":
                if sequence[i] == sequence[j]:
                    flag = True
                    break
        if flag:
            break
print(flag)
