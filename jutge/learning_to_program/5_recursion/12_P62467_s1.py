# https://jutge.org/problems/P62467_en


def bars1(n, i=0, seq=""):
    if i == n + 1:
        print(*seq.split(), sep="\n")
    else:
        return bars1(n, i + 1, seq + "*" * i + "\n" + seq)


bars1(n=int(input()))
