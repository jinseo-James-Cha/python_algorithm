def solution(picture, k):
    answer = []
    for p in picture:
        temp = ""
        for x in p:
            temp += x * k
        
        for a in range(k):
            answer.append(temp)
        
    return answer