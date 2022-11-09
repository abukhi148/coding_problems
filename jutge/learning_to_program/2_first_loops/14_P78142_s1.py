# https://jutge.org/problems/P78142_en/statement
numbers = list(map(float, input().rsplit()))
print("{:.2f}".format(round(sum(numbers) / len(numbers), 2)))
