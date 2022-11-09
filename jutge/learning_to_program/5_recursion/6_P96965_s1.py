# https://jutge.org/problems/P96965_en


def sum_of_digits(x):
    return sum(list(map(int, list(str(x)))))


def reduction_of_digits(x):
    return x if str(x)[1:] == "" else reduction_of_digits(sum_of_digits(x))
