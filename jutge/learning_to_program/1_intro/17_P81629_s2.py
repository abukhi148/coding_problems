# https://jutge.org/problems/P81629_en/statement
e, c = tuple(map(int, input().rsplit()))
x = [
    (print(f"Banknotes of {i} euros: {e // i}"), e := e % i)
    for i in [500, 200, 100, 50, 20, 10, 5]
]
y = [
    (print(f"Coins of {i} {'euros' if i != 1 else 'euro'}: {e // i}"), e := e % i)
    for i in [2, 1]
]
z = [
    (print(f"Coins of {i} {'cents' if i != 1 else 'cent'}: {c // i}"), c := c % i)
    for i in [50, 20, 10, 5, 2, 1]
]
