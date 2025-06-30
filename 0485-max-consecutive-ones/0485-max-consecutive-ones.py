class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        temp = 0
        for n in nums:
            if n != 1:
                temp = 0
            else:
                temp += 1
                m = max(temp, m)
        return m