# bottom - up
MOD = 10007
N = int(input())

cache = [[-1] * 1001 for _ in range(1001)]

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
        cache[i][j] %= 10007

print(cache[N][K])