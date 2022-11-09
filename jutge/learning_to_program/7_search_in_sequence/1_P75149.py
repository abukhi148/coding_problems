# https://jutge.org/problems/P75149_en
sentence = "".join(input().split())
a = False
for i in sentence:
    if i == "a":
        a = True
        break
print("yes" if a else "no")
