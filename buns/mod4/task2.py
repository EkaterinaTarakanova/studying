def number_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return number_power(a * a, n // 2)
    else:
        return a * number_power(a, n - 1)

a, n = int(input()), int(input())
print(number_power(a, n))