class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # unique
        # maximum sum
        res = 0
        seen = set()
        for num in nums:
            if num not in seen and num > 0:
                seen.add(num)
                res += num
        return res if seen else max(nums)