def solution(n, k):
    # return [x for x in range(1, n+1) if x % k == 0] 1부터 안해도되네..
    return [x for x in range(k, n+1, k)]