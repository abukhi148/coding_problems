# https://jutge.org/problems/P22467_en

# TODO: optimize the time of execution
import timeit


def is_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    else:
        return is_prime(n, i + 1)


def sum_of_digits(n):
    return sum(list(map(int, list(str(n)))))


def is_perfect_prime(n):
    if not is_prime(n):
        return False
    else:
        return True if n < 10 else is_perfect_prime(sum_of_digits(n))


for x in [977, 978, 0, 11, 9662, 3101, 2]:
    start = timeit.default_timer()
    print(x, is_perfect_prime(x))
    end = timeit.default_timer()
    print(end - start)
