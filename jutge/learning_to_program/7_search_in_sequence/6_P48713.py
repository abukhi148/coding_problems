# https://jutge.org/problems/P48713_en
import sys, math


def is_prime(n):
    if n <= 2:
        return True if n == 2 else False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


nums = list(map(int, sys.stdin.read().split()))
for n in nums[1:]:
    print(f"{n} is prime" if is_prime(n) else f"{n} is not prime")
