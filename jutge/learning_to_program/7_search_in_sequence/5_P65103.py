# https://jutge.org/problems/P65103_en
import sys

nums = [int(x) for x in sys.stdin.read().split() if x]
idx = nums[0]
nums = nums[1:]
if 0 <= idx - 1 < len(nums):
    print(f"At the position {idx} there is a(n) {nums[idx - 1]}.")
else:
    print("Incorrect position.")
