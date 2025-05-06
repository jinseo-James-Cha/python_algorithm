def solution(n):
    a = min(n, 6)
    while a <= 100 * 6:
        if a % 6 == 0 and a % n == 0:
            answer = a
            break
        else:
            a += min(n, 6)
    
    return answer // 6