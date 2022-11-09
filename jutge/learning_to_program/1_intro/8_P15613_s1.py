# https://jutge.org/problems/P15613_en
temperature = int(input())
if temperature > 30:
    print("it's hot")
    if temperature >= 100:
        print("water would boil")
elif temperature < 10:
    print("it's cold")
    if temperature <= 0:
        print("water would freeze")
else:
    print("it's ok")
