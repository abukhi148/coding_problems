# https://jutge.org/problems/P31111_en


def p_com(p):
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0 and "(" == stack[-1]:
                stack.pop()
            else:
                return "no"
    return "yes" if len(stack) == 0 else "no"


print(p_com(input()))

# Todo: read more about stacks and how to use them -> https://favtutor.com/blogs/valid-parentheses
