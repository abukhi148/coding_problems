# https://jutge.org/problems/P98960_en/statement
letter = input()
if letter.isupper():
    letter = letter.lower()
else:
    letter = letter.upper()
print(letter)
