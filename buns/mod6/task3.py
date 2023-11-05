def is_armstrong_number(num):
    num_str = str(num)
    n = len(num_str)
    return sum(int(digit)**n for digit in num_str) == num

def get_armstrong_numbers():
    num = 10
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1

armstrong_generator = get_armstrong_numbers()
for i in range(8):
    print(next(armstrong_generator), end=' ')
