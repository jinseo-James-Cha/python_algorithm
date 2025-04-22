# set - set 할 수도 있구나?!
# 5의 배수단위로만 interval setting

# def solution(l, r):
#     answer = []
#     for num in range(l, r+1):
#         num_str = str(num)
#         if not set(num_str) - set(['0', '5']):
#             answer.append(num)
            
#     return answer if answer else [-1]    

# 다른방식으로도 적어보자
def solution(l, r):
    answer = []
    letters = ['0', '5']
    
    for target in range(l, r + 1):
        flag = False
        target_str = str(target)
        for target_letter in target_str:
            if target_letter in letters:
                flag = True
            else:
                flag = False
                break
        if flag:
            answer.append(target)
            
    return answer if answer else [-1]
 