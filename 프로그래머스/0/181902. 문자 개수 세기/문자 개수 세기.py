# 난 이 방법이 더 좋은거같아
def solution(my_string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    return [my_string.count(a) for a in alphabets.upper() + alphabets]


# ord(ch)는 문자의 아스키코드 숫자
# def solution(my_string):
#     lower_case = [0] * 26
#     upper_case = [0] * 26
    
#     a_num = ord('a')
#     z_num = ord('z')
#     A_num = ord('A')
#     for target in my_string:
#         target_num = ord(target)
#         if target_num >= a_num and target_num <= z_num:
#             lower_case[target_num - (a_num)] += 1
#         else:
#             upper_case[target_num - (A_num)] += 1

#     return upper_case + lower_case