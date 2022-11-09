# https://jutge.org/problems/P59539_en
harmonic = 0
[harmonic := harmonic + (1 / i) for i in range(1, int(input()) + 1)]
print("{:.4f}".format(harmonic))
# TODO: make it loop faster for bigger values
