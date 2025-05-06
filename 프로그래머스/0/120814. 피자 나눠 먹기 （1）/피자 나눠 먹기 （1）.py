def solution(n):
    a = 1 if n % 7 != 0 else 0
    return n // 7 + a