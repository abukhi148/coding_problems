# https://jutge.org/problems/P89078_en
nums = list(map(int, input().split()))
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print(i + 1)
        break
