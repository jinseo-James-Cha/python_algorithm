N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

answer = 0
for coin in coins:
    answer += K // coin
    K %= coin
    
print(answer)