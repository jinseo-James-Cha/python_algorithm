# 4 same num p          -> 1111 * p
# 3 same num p, 1 num q -> (10 * p + q)**2
# 2 p, 2 q              -> (p + q) * |p - q|
# 2 p, 1 q, 1 r         -> q * r
# all differ            -> min num

from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]  # 주사위 결과를 리스트에 저장
    count = Counter(dice)  # 각 숫자가 몇 번 나왔는지 세기
    nums = list(count.keys())  # 나온 숫자들 (중복 제거된 형태)
    freqs = list(count.values())  # 각 숫자의 빈도수 리스트

    if len(count) == 1:  # 네 개가 전부 같은 숫자일 경우
        return 1111 * nums[0]

    elif len(count) == 2:
        if 3 in freqs:  # 세 개가 같은 숫자일 경우 (3개, 1개)
            p = nums[freqs.index(3)]  # 3번 나온 숫자
            q = nums[freqs.index(1)]  # 1번 나온 숫자
            return (10 * p + q) ** 2
        else:  # 두 쌍으로 나뉜 경우 (2개, 2개)
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])

    elif len(count) == 3:  # 2개는 같은 숫자, 나머지는 다를 경우 (2,1,1)
        p = [num for num in count if count[num] == 2][0]  # 2번 나온 숫자
        q, r = [num for num in count if count[num] == 1]  # 1번씩 나온 숫자들
        return q * r  # 1번씩 나온 숫자끼리 곱함

    return min(dice)  # 가장 작은 수를 점수로 반환