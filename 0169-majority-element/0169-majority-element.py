# n = len(nums)
# n / 2 > majority num
# len 7 includes more than 4

# O(1) in space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        m = 0
        answer = 0
        for k, v in d.items():
            if v > m:
                m = v
                answer = k
        return answer

        # memory limit exceeded
        # answer = [0] * (max(nums) + 1)
        
        # for n in nums:
        #     answer[n] += 1

        # return answer.index(max(answer))

