class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 3 4
        # 1 = right 2 * 3 * 4
        # 2 = left1 *  right3 * 4 
        # 3 = left1*2 * right4
        # 4 = left 1*2*3

        # -> way
        res = [1] * len(nums)
        curr = nums[0]
        for i in range(1, len(nums)):
            res[i] = curr
            curr *= nums[i]

        curr = nums[-1]
        for j in range(len(nums)-2,-1, -1): # 2
            res[j] *= curr
            curr *= nums[j]
        
        return res

