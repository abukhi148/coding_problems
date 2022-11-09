# https://jutge.org/problems/P90226_en/statement
a, b = tuple(input().rsplit())
print(f"{a} > {b}") if a > b else (
    print(f"{a} < {b}") if a < b else print(f"{a} = {b}")
)
