# https://jutge.org/problems/P42042_en
letter = input()
vowels = "aeiouAEIOU"
if letter.isupper():
    print("uppercase")
else:
    print("lowercase")

if letter in vowels:
    print("vowel")
else:
    print("consonant")
