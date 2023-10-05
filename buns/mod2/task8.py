def counter_i(s, i):
    counter = 0
    for char in s:
        if char == i:
            counter += 1
        else:
            break
    return counter

string = input("Введите через запятую строку и символ")
comma = string.find(",")
s = str(string[:comma])
i = str(string[comma+1:])
print(counter_i(s, i))