def counter(string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    vowel_count = 0
    consonant_count = 0
    for letter in string:
        if ('а' <= letter <= 'я') or ('А' <= letter <= 'Я'):
            if letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

string = input("Введите строку")
rowel_count, consonant_count = counter(string)
print(rowel_count, consonant_count)

