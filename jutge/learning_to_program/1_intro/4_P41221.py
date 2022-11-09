# https://jutge.org/problems/P41221_en/
numbers = input().rsplit()
while len(numbers) < 3:
    numbers += input().rsplit()
print(sum(list(map(int, numbers))))
