# https://jutge.org/problems/P58153_en
import sys

for n, m in [tuple(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if x]:
    hn = sum((1 / i) for i in range(m + 1, n + 1))
    print("{:.10f}".format(hn))
