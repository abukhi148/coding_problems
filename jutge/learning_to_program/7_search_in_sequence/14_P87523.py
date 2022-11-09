# https://jutge.org/problems/P87523_en/statement
s = input()
stack = list('olleh')
for i in s:
    if not stack:
        break
    elif i != stack[-1]:
        stack = list('olleh')
    if i == stack[-1]:
        stack.pop()
print('hello') if not stack else print('bye')
