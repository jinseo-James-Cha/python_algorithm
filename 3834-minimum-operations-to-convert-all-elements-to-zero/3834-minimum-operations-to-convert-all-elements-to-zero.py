class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # all num in nums >= 0
        # operate make them 0
        # 1 operation select subarray [i, j]
        # return minimum

        # two pointers smell

        # left keeps holding minium
        # right keeps moving forward if it is not 0
        s = []
        res = 0
        for num in nums:
            while s and s[-1] > num:
                s.pop()
            if num == 0:
                continue
            if not s or s[-1] < num:
                res += 1
                s.append(num)
        return res
