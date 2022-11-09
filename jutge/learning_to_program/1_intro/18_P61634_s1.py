# https://jutge.org/problems/P61634_en
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print("YES")
elif year % 100 == 0 and (year / 100) % 4 == 0.0:
    print("YES")
else:
    print("NO")
