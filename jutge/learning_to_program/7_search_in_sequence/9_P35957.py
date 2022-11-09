# https://jutge.org/problems/P35957_en
import sys

inp = list(sys.stdin.read().split())
l, nums = int(inp[0]), inp[1:]
r = '='
for i in range(1, l*2):
    p = nums[i - 1][len(nums[i - 1]) // 2]
    c = nums[i][len(nums[i]) // 2]
    if len(nums[i - 1]) % 2 == 0:
        r = 'B' if (i - 1) % 2 == 0 else 'A'
        break
    elif len(nums[i]) % 2 == 0 or p != c:
        r = 'B' if i % 2 == 0 else 'A'
        break
print(r)

# Todo: this can done more elegantly
