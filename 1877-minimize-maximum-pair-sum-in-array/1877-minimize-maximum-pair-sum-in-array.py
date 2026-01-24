class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # minimize sum..
        # sort and two pointer from left and right
        # min + max .. -> minimize pair sum

        """
        3 5 4 2 4 6

        2 3 4 4 5 6

        2 6, 3 5, 4 4 
        """
        nums.sort()
        left = 0
        right = len(nums) - 1

        min_pair_sum = float('-inf')
        while left < right:
            pair_sum = nums[left] + nums[right]
            min_pair_sum = max(min_pair_sum, pair_sum)

            left += 1
            right -= 1
        return min_pair_sum