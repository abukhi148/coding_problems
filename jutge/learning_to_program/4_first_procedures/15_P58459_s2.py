# https://jutge.org/problems/P58459_en


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)


def get_days_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30


def is_valid_date(day, month, year):
    return (1 <= month <= 12) and 1 <= day <= get_days_month(month, year)
