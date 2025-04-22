# 4 same num p          -> 1111 * p
# 3 same num p, 1 num q -> (10 * p + q)**2
# 2 p, 2 q              -> (p + q) * |p - q|
# 2 p, 1 q, 1 r         -> q * r
# all differ            -> min num

from collections import Counter

def solution(a, b, c, d):
    count = Counter([a, b, c, d]) 
    nums = list(count.keys())
    freqs = list(count.values())

    if len(count) == 1:
        return 1111 * nums[0]
    elif len(count) == 2:
        if 3 in freqs:
            p = nums[freqs.index(3)]
            q = nums[freqs.index(1)]
            return (10 * p + q) ** 2
        else:
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])
    elif len(count) == 3:
        q, r = [num for num in count if count[num] == 1]
        return q * r 

    return min([a, b, c, d])