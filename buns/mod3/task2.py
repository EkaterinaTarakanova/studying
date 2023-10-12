a = int(input())
binary, octal, hexadecimal = bin(a), oct(a), hex(a)
print(binary[2:], octal[2:], hexadecimal[2:], sep=", ")