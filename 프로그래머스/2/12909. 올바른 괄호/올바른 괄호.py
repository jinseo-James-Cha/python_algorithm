def solution(s):
    stack = []
    for a in s:
        if a == "(":
            stack.append(a)
        elif stack:
            stack.pop()
        else:
            return False

    return not stack