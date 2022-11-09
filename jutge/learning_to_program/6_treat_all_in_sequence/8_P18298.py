# https://jutge.org/problems/P18298_en
import sys

roman_nums = {
    1: {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    },
    10: {"I": "X", "V": "L", "X": "C"},
    100: {"I": "C", "V": "D", "X": "M"},
    1000: {"I": "M"},
}

nums = [int(x) for x in sys.stdin.read().split() if x]
for n in nums:
    r_n, no, divs = list(), n, [1000, 100, 10, 1][-len(str(n)) :]
    for d in divs:
        q, n = divmod(n, d)
        r = roman_nums[1][q]
        if d > 1:
            r = "".join([roman_nums[d].get(i, i) for i in r])
        r_n.append(r)
    print(f"{no} = {''.join(r_n)}")
# TODO: revise
