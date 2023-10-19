def count_letters(filename):
    char_count = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            for char in line:
                if char.isalpha():
                    if char in char_count:
                        char_count[char] += 1
                    else:
                        char_count[char] = 1
    sorted_char = sorted(char_count.items(), key=lambda x: x[1])
    return sorted_char

filename = input()
output_filename = input()
sorted_char = count_letters(filename)
with open(output_filename, 'w') as file:
    for char, count in sorted_char:
        file.write(f"{char}: {count} \n")