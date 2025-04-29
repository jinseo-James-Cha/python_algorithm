N = int(input()) 
money_requests = list(map(int, input().split()))
M = int(input())


left = 0
right = max(money_requests)
answer = 0

def is_possible(mid):
    return sum([min(r, mid) for r in money_requests]) <= M


while left <= right:
    mid = (left + right) // 2
    
    if is_possible(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
    
print(answer)