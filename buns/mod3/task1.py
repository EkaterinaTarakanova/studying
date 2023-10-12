a , b , c = map(int, (input().split()))
medium = a + b + c - max(a, b, c) - min(a, b, c)
print(medium)