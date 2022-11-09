# https://jutge.org/problems/P57548_en
n = input().rsplit()
while len(n) < 2:
    n += input().rsplit()
print(sum(list(map(int, n))))
