# https://jutge.org/problems/P95401_en/statement


def is_leap_year(year):
    leap_y = (
        True
        if (year % 4 == 0 and year % 100 != 0)
        or (year % 100 == 0 and (year / 100) % 4 == 0.0)
        else False
    )
    return leap_y
