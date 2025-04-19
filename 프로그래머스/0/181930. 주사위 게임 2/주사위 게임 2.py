# all dif -> **1
# two same -> **2
# three(all) same -> **3
def solution(a, b, c):
    answer = 1
    count_same_number = 1
    if a == b and b == c:
        count_same_number = 3
    elif (not a == b and a == c) or (a == b and not a == c) or (not a == b and b ==c):
        count_same_number = 2
        
    for i in range(1, count_same_number+1):
        answer *= a**i + b**i + c**i
    
    return answer