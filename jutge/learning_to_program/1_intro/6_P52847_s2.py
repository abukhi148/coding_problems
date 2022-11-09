# https://jutge.org/problems/P52847_en/
# using loops
numbers = input().rsplit()
numbers = list(map(int, numbers))
maximum = numbers[0]
for number in numbers[1:]:
    if number > maximum:
        maximum = number
print(maximum)
