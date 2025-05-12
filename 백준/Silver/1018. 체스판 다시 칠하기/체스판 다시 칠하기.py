N,M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 64 # more than possibility

def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2: # odd 
                if board[y + i][x + j] == bw:
                    cnt += 1
            else:
                if board[y + i][x + j] != bw:
                    cnt += 1
    ans = min(ans, cnt)

for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, 'W')
        fill(i, j, 'B')

print(ans)