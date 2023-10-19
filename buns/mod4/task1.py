def check_numbers(string):
    if len(set(string)) == 1:
        return "Все числа равны"
    elif len(set(string)) == len(string):
        return "Все числа разные"
    else:
        return "Есть равные и не равные числа"

string = input().split()
print(check_numbers(string))
