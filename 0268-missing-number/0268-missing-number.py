class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Follow up: 
        # Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


        # v1
        nums.sort()
        res = len(nums)
        for i, num in enumerate(nums):
            if i != num:
                res = i
                break
        return res
