def solution(arr):
    check=[]
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i]==2:
                check.append(i)
    return arr[check[0]:check[-1]+1]


# 내 풀이도 정답이지만 엉성하다..
# def solution(arr):
#     first_two = -1
#     second_two = -1
    
#     for i in range(len(arr)):
#         if arr[i] == 2:
#             if first_two < 0:
#                 first_two = i
#             else:
#                 second_two = i
    
#     if first_two < 0 and second_two < 0:
#         return [-1]
#     elif first_two > 0 and second_two < 0:
#         return [arr[first_two]]
    
#     return arr[first_two: second_two + 1]