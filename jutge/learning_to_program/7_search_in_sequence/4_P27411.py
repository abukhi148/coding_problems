# https://jutge.org/problems/P27411_en

idx = int(input())
nums = list(map(int, input().split()))[:-1]
if 0 <= idx - 1 < len(nums):
    print(f"At the position {idx} there is a(n) {nums[idx - 1]}.")
else:
    print("Incorrect position.")
