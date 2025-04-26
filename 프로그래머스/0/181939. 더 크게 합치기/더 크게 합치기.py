def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# solution 2
#     str_ab = str(a) + str(b)
#     str_ba = str(b) + str(a)
    
#     int_ab = int(str_ab)
#     int_ba = int(str_ba)
    
#     return int_ab if int_ab >= int_ba else int_ba