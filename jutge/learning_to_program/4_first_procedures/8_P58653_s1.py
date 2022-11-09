# https://jutge.org/problems/P58653_en/statement

char = input()
vowels = "aeiouAEIOU"
print(f"letter('{char}') = {str(char.isalpha()).lower()}")
print(f"vowel('{char}') = {str(char in vowels).lower()}")
print(
    f"consonant('{char}') = true"
) if char not in vowels and char.isalpha() else print(f"consonant('{char}') = false")
print(f"uppercase('{char}') = {str(char.isupper()).lower()}")
print(f"lowercase('{char}') = {str(char.islower()).lower()}")
print(f"digit('{char}') = {str(char.isdigit()).lower()}")
