# Top - down 
import sys
sys.setrecursionlimit(10 ** 7)

# MOD = 10007
# N, K = map(int, input().split())

# # memoization
# cache = [[0] * 1001 for _ in range(1001)]

# def bino(n,r):
#     if cache[n][r]:
#         return cache[n][r]

#     if r == 0 or r == n:
#         cache[n][r] = 1
#     else:
#         cache[n][r] = bino(n-1, r-1) + bino(n-1, r)
#         cache[n][r] %= MOD

#     return cache[n][r]

# print(bino(N, K))



# Bottom up
MOD = 10007
N, K = map(int, input().split())

cache = [[0] * 1001 for _ in range(1001)]

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
        cache[i][j] %= 10007

print(cache[N][K])