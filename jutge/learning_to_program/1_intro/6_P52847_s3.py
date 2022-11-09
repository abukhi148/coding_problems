# https://jutge.org/problems/P52847_en/
# walrus operator (:=)
numbers = list(map(int, input().rsplit()))
maximum = numbers[0]
m = [maximum := number for number in numbers[1:] if number >= maximum]
print(maximum)
