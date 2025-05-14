def check_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] !=  s[-1]:
        return False
    return check_palindrome(s[1:-1])


n = int(input())
inputs = [input() for _ in range(n)]
for a in inputs:
    check_palindrome(a)