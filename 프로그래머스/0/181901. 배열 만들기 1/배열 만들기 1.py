def solution(n, k):
    return [x for x in range(1, n+1) if x % k == 0]