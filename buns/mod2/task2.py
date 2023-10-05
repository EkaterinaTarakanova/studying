def rounder(number):
    multiplier = 10**2
    rounded_number = int (number * multiplier + 0.5)
    return rounded_number / multiplier

side = float(input())
perimetr = rounder(side * 4)
area = rounder(side ** 2)
diagonal = rounder(2 ** 0.5 * side)
print(perimetr, area, diagonal, sep = ", ")

