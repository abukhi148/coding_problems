# https://jutge.org/problems/P72484_en
n = int(input())
sp, st = list(range(n)), list(range(1, 2 * n, 2))
sp, st = (sp[::-1] + sp[1:], st[:-1] + st[::-1])
for sp, st in list(map(lambda x, y: (x, y), sp, st)):
    print(f"{sp * ' '}{st * '*'}")
