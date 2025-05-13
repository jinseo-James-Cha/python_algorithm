# BOJ 1158
# deque를 이용하자
# 인덱스가 넘어가면 뒤에다가 넣자
# 인덱스가 일치하면 answer에 담자
from collections import deque

def josephus_problem(n, k):
    answer =[]
    dq = deque([a for a in range(1, n+1)])

    temp = 1
    while len(dq) > 0:
        if temp == k:
            answer.append(dq.popleft())
            temp = 1
        else:
            d_temp = dq.popleft()
            dq.append(d_temp)
            temp += 1
    
    print("<" + ", ".join(map(str, answer)) + ">")

n, k = map(int, input().split())
josephus_problem(n, k)