# https://jutge.org/problems/P15613_en
temperature = int(input())
message = ""
message += (
    "it's hot" if temperature > 30 else ("it's cold" if temperature < 10 else "it's ok")
)
message += (
    "\nwater would freeze"
    if (temperature <= 0)
    else ("\nwater would boil" if (temperature >= 100) else "")
)
print(message)
