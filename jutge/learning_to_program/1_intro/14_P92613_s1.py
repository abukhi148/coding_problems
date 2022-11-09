# https://jutge.org/problems/P92613_en/statement
import math

number = float(input())
if number - math.floor(number) == 0.5:
    rounded = math.floor(number) + 1
else:
    rounded = round(number)
print(math.floor(number), math.ceil(number), rounded)
