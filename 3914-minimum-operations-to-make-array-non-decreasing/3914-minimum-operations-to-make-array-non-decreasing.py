class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        n = len(nums)

        subarray nums[l...r] 
        increase each element by x, where x is positive

        Make non-decreasing is >= prev

        Input: nums = [3,3,2,1]
        when 3  > 2 -> 1
        3 <= 3 <= 2+1 <= 1+1 
        
        when 2+1 > 1+1
        3 <= 3 <= 2+1 <= 1+1+1
    
        ----------------------
        Input: nums = [5,1,2,3]

        when 5 > 1 -> 4
        5 <= x+4 <= x+4 <= x+4, after first we add all right elements +4
        5 <= 6 <= 2+4 <= 3+4
        """
        n = len(nums)
        operations = 0

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                operations += nums[i] - nums[i+1]

        return operations