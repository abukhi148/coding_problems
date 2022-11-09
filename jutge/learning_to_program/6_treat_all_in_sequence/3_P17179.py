# https://jutge.org/problems/P17179_en

import sys

nl = [[float(i) for i in x.split()] for x in sys.stdin.read().split("\n")[1:]]
for i in nl:
    i = i[1:]
    print(
        "{:.4f}".format(min(i)),
        "{:.4f}".format(max(i)),
        "{:.4f}".format(sum(i) / len(i)),
    )  # TODO: remove repetition of print to make it more simple
