# https://jutge.org/problems/P67723_en/statement
a, b = tuple(map(int, input().rsplit()))
(x, y) = (a, b)
while y != 0:
    (x, y) = (y, x % y)
print(f"The gcd of {a} and {b} is {x}.")
