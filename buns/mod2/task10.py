def new_word(words):
    new_word = ""
    word = ""
    for letter in words:
        if letter != " ":
            word += letter
        else:
            if len(word) > 0:
                last_letter = word[-1]
                new_word += last_letter
            word = ""
    if len(word) > 0:
        last_letter = word[-1]
        new_word += last_letter
    return new_word

words = input("Введите слова через пробел")
new_word = new_word(words)
print(new_word)
