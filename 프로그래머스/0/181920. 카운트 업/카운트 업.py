# 방법 1 return list(range(start_num, end_num + 1))
# 방법 2 return [num for num in range(start_num, end_num + 1)]

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num +  1):
        answer.append(i)
    return answer