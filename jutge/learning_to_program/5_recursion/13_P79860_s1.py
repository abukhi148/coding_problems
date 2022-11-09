# https://jutge.org/problems/P79860_en


def bars2(n, i=0, seq=""):
    if i == n + 1:
        print(*seq.split(), sep="\n")
    else:
        return bars2(n, i + 1, "*" * i + "\n" + 2 * seq)


bars2(n=int(input()))
