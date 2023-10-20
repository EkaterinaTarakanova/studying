def make_palindrome(word):
    char_count = {}
    for char in word:
        if char_count.get(char) is None:
            char_count[char] = 1
        else:
            char_count[char] += 1
    unique_char = len(char_count)
    even_repetitions = 0
    odd_char = ''
    for char, count in char_count.items():
        if count % 2 == 0:
            even_repetitions += 1
        else:
            odd_char = char
    palindrome_half = ''
    for char, count in char_count.items():
        palindrome_half += char * (count // 2)
    if even_repetitions == unique_char or even_repetitions == unique_char - 1:
        palindrome = palindrome_half + odd_char + palindrome_half[::-1]
        print(palindrome)
    else:
        print("Невозможно составить палиндром")

word = input()
make_palindrome(word)
