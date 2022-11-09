# https://jutge.org/problems/P59539_en
n = int(input())
harmonic = 0
for i in range(1, n + 1):
    harmonic = harmonic + 1 / i
print("{:.4f}".format(harmonic))
