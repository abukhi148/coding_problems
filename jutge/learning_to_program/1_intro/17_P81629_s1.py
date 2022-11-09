# https://jutge.org/problems/P81629_en/statement
e, c = tuple(map(int, input().rsplit()))

for i in [500, 200, 100, 50, 20, 10, 5]:
    q = e // i
    e = e % i
    print(f"Banknotes of {i} euros: {q}")

for i in [2, 1]:
    q = e // i
    e = e % i
    print(f"Coins of {i} {'euros' if i != 1 else 'euro'}: {q}")

for i in [50, 20, 10, 5, 2, 1]:
    q = c // i
    c = c % i
    print(f"Coins of {i} {'cents' if i != 1 else 'cent'}: {q}")
