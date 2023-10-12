string = input().split()
new_word = ''.join(word[-1] for word in string)
print(new_word)