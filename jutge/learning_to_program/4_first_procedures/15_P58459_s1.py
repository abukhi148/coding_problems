# https://jutge.org/problems/P58459_en


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and (year / 100) % 4 == 0.0:
        return True
    else:
        return False


def is_valid_date(day, month, year):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    if 1800 <= year <= 9999:
        if 1 <= month <= 12:
            if month in days_31:
                if 1 <= day <= 31:
                    result = "Correct Date"
                else:
                    result = "Incorrect Date"
            elif month in days_30:
                if 1 <= day <= 30:
                    result = "Correct Date"
                else:
                    result = "Incorrect Date"
            elif month == 2 and leap_year(year=year):
                if 1 <= day <= 29:
                    result = "Correct Date"
                else:
                    result = "Incorrect Date"
            elif month == 2 and not leap_year(year=year):
                if 1 <= day <= 28:
                    result = "Correct Date"
                else:
                    result = "Incorrect Date"
            else:
                result = "Incorrect Date"
        else:
            result = "Incorrect Date"
    else:
        result = "Incorrect Date"
    if result == "Correct Date":
        return True
    else:
        return False
