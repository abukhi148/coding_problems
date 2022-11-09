# https://jutge.org/problems/P42042_en
letter = input()
print("uppercase") if letter.isupper() else print("lowercase")
print("vowel") if letter in "aeiouAEIOU" else print("consonant")
