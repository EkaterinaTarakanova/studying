def cleaned_phone_number(phone_number):
    cleaned_number = ''
    for char in phone_number:
        if '0' <= char <= '9' or char == '+':
            cleaned_number += char
    return cleaned_number

phone_number = input("Введите номер телефона")
print(cleaned_phone_number(phone_number))
