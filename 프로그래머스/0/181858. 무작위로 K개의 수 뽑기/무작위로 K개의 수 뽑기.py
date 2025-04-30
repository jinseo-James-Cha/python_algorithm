def solution(arr, k):
    i = 0
    answer = []
    while len(answer) < k and i < len(arr):
        if not arr[i] in answer:
            answer.append(arr[i])
        i += 1
    
    for _ in range(k -len(answer)):
        answer.append(-1)
    
    return answer