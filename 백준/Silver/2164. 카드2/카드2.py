from collections import deque

n = int(input())
dq = deque(range(1, n+1))

while len(dq) > 1:
    dq.popleft()
    if len(dq) > 1:
        n = dq.popleft()
        dq.append(n)
    else:
        break

print(dq[0] if dq else n)
