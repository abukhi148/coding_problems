# https://jutge.org/problems/P89872_en
import sys

words = sorted(list(set([x for x in sys.stdin.read().split() if x])), reverse=True)
print(words[1])
# Todo: solve without the sorted method
