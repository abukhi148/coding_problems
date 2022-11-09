# https://jutge.org/problems/P90226_en/statement
a, b = tuple(input().rsplit())
if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")
