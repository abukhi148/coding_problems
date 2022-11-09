# https://jutge.org/problems/P10694_en


def bars3(n, i=0, seq=""):
    if i == n + 1:
        print(*seq.split(), sep="\n")
    else:
        return bars3(n, i + 1, 2 * seq + "*" * i + "\n")


bars3(n=int(input()))
