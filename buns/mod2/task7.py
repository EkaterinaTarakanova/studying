def counter(string):
    zero_counter = 0
    one_counter = 0
    for digit in string:
        if (digit == '0'):
            zero_counter += 1
        elif (digit == '1'):
            one_counter += 1
    if (zero_counter == one_counter):
        return 'yes'
    else:
        return 'no'

string = input("Введите строку из нулей и единиц")
print(counter(string))