import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10007
N, K = map(int, input().split())

# memoization
cache = [[0] * 1001 for _ in range(1001)]

def bino(n,r):
    if cache[n][r]:
        return cache[n][r]

    if r == 0 or r == n:
        cache[n][r] = 1
    else:
        cache[n][r] = bino(n-1, r-1) + bino(n-1, r)
        cache[n][r] %= MOD

    return cache[n][r]

print(bino(N, K))