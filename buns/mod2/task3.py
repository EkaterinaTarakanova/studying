numbers = input("Введите три целых числа через пробел")
space1 = numbers.find(" ")
a = int(numbers[:space1])
space2 = numbers.find(" ", space1 + 1)
b = int(numbers[space1+1:space2])
c = int(numbers[space2 + 1:])

if (a < b < c) or (c < b < a):
    print(b)
elif (b < a < c) or (c < a < b):
    print(a)
else:
    print(c)