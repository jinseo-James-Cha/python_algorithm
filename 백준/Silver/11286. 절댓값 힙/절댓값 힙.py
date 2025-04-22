import heapq
import sys

input = sys.stdin.readline
hp = []
for _ in range(int(input())):
    ip = int(input())
    if not ip == 0:
        heapq.heappush(hp, (abs(ip), ip))
    else:
        if hp:
            print(heapq.heappop(hp)[1])
        else:
            print(0)