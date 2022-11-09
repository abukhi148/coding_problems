# https://jutge.org/problems/P61634_en
year = int(input())
print("YES") if year % 4 == 0 and year % 100 != 0 else (
    print("YES") if year % 100 == 0 and (year / 100) % 4 == 0 else print("NO")
)
