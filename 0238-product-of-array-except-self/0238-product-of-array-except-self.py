class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        1 2 3 4

        0 : 1 2 3
        1 : 0 2 3 
        2 : 0 1 3
        3 : 0 1 2

        -> one pass
        res[i] = total_product
        total_product * nums[i]

        <- one pass
        """
        
        # to right
        curr = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = curr
            curr *= nums[i]

        # 24 12 8 6
        # 
        # to left
        curr = nums[-1]
        for j in range(len(nums)-2, -1, -1):
            res[j] = res[j] * curr # 2 * 4 -> 1 * 12 -> 1 * 24
            curr *= nums[j] # 4 * 3 12 24 -> 
        return res
