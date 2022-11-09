# https://jutge.org/problems/P29448_en/statement
import sys


def leap_year(year):
    r = (
        True
        if year % 4 == 0 and year % 100 != 0
        else (True if year % 100 == 0 and (year / 100) % 4 == 0.0 else False)
    )
    return r


dates = [
    tuple(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if len(x) > 1
]
days_31 = [1, 3, 5, 7, 8, 10, 12]

for day, month, year in dates:
    r = False
    if (1800 <= year <= 9999) and (1 <= month <= 12):
        if month == 2:
            r = (
                True
                if 1 <= day <= 29 and leap_year(year=year)
                else (True if 1 <= day <= 28 else r)
            )
        elif month in days_31:
            r = True if 1 <= day <= 31 else r
        elif month not in days_31:
            r = True if 1 <= day <= 30 else r
    print("Correct Date") if r else print("Incorrect Date")
