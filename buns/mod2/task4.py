def converter(number, base):
    digits = '0123456789ABCDEF'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result

number = int(input("Введите натуральное число в десятичной системе"))
if (number <= 0):
    print("Неверный ввод")
else:
    print(converter(number, 2), converter(number, 8), converter(number, 16), sep = ', ')