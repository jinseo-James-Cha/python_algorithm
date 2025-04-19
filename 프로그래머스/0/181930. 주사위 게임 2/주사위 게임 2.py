# set을 만들면 중복이 사라지고 다른것만 나온다 와우
# set([a,b,c])하고 len하면 중복이 몇개있는지 안다.

# all dif -> **1
# two same -> **2
# three(all) same -> **3
def solution(a, b, c):
#     answer = 1
#     count_same_number = 1
#     if a == b and b == c:
#         count_same_number = 3
#     elif (not a == b and a == c) or (a == b and not a == c) or (not a == b and b ==c):
#         count_same_number = 2
        
#     for i in range(1, count_same_number+1):
#         answer *= a**i + b**i + c**i

    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)

    
    return answer