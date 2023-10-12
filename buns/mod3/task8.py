phone_number = input()
phone_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
print(phone_number)