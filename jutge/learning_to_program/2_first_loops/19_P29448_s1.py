# https://jutge.org/problems/P29448_en/statement
import sys


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and (year / 100) % 4 == 0.0:
        return True
    else:
        return False


dates = [
    tuple(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if len(x) > 1
]

days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11]

for day, month, year in dates:
    if 1800 <= year <= 9999:
        if 1 <= month <= 12:
            if month in days_31:
                if 1 <= day <= 31:
                    print("Correct Date")
                else:
                    print("Incorrect Date")
            elif month in days_30:
                if 1 <= day <= 30:
                    print("Correct Date")
                else:
                    print("Incorrect Date")
            elif month == 2 and leap_year(year=year):
                if 1 <= day <= 29:
                    print("Correct Date")
                else:
                    print("Incorrect Date")
            elif month == 2 and not leap_year(year=year):
                if 1 <= day <= 28:
                    print("Correct Date")
                else:
                    print("Incorrect Date")
            else:
                print("Incorrect Date")
        else:
            print("Incorrect Date")
    else:
        print("Incorrect Date")
