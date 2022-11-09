# https://jutge.org/problems/P50095_en
import sys, math


def is_prime(n):
    if n <= 2:
        return True if n == 2 else False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


nums = list(map(int, sys.stdin.read().split()))
for n in nums:
    if is_prime(n):
        next_prime = False
        while not next_prime:
            n += 1
            next_prime = is_prime(n)
        print(n)

# Todo: read more about prime optimization -> https://geekflare.com/prime-number-in-python/
