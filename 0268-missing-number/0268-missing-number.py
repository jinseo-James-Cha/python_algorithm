class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        for i in range(m):
            if i not in nums:
                return i
        return m