# for loop을 써야할까?
# 다른방법은 없을까..

# 곱하는건 for loop이 맞는듯하다
# 하지만 정수의 리스트를 더하는건 sum(num_list)

def solution(num_list):
    # s = 0
    s = sum(num_list)
    mul = 1
    for i in range(len(num_list)):
        # s += num_list[i]
        mul *= num_list[i]

    return int(mul < s**2)