# version 2 by heapq
import heapq

def solution(myString):
    answer = []
    for a in myString.split("x"):
        if a:
            heapq.heappush(answer,a)
    
    # return answer
    return [heapq.heappop(answer) for _ in range(len(answer))]
    
    


# def solution(myString):
#     return sorted([a for a in myString.split("x") if a])