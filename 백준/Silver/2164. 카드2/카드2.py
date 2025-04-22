from collections import deque

dq = deque()
n = int(input())
for i in range(1, n+1):
    dq.append(i)
while len(dq) > 1:
    dq.popleft()
    if len(dq) > 1:
        n = dq.popleft()
        dq.append(n)
    else:
        break

print(dq[0] if dq else n)
