# for loop을 써야할까?
# 다른방법은 없을까..

def solution(num_list):
    sum = 0
    mul = 1
    for i in range(len(num_list)):
        sum += num_list[i]
        mul *= num_list[i]

    return int(mul < sum**2)