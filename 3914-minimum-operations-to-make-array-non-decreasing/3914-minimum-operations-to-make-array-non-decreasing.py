class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        n = len(nums)

        subarray nums[l...r] 
        increase each element by x, where x is positive

        Make non-decreasing is >= prev

        Input: nums = [5,1,2,3]

        n = 4

        range(3)
        """
        n = len(nums)
        operations = 0

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                operations += nums[i] - nums[i+1]  # Add the size of the drop

        return operations