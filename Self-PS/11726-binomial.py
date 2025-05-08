# bottom - up
MOD = 10007
N = int(input())

cache = [0] * 1001
cache[1] = 1
cache[2] = 2
for i in range(3, N + 1):
    cache[i] = (cache[i-1] + cache[i-2]) % MOD

print(cache[N])