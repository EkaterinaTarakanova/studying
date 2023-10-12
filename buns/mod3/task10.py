size = int(input())
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j == size:
            print(j)
        else:
            print(j, end=', ')
print()
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j == size:
            print(j)
        else:
            print(i, end=', ')
