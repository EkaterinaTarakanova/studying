sequence = input()
result = any(sequence.count(char) > 1 for char in sequence)
print(result)
