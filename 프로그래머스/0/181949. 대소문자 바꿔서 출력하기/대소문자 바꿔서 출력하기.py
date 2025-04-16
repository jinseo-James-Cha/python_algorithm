str = input()
result = []
for letter in str:
    if letter >= 'A' and letter <= 'Z':
        result.append(letter.lower())
    else:
        result.append(letter.upper())

print(''.join(result))