class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # idea is all multiple by i-1 * all multiple by (i+1)
        # im the middle and multiple left and right
        
        # 1. left first
        # 1 2 3 4 -> 1 
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        
        # 2. right 
        right_product = 1
        for i in range(n - 1 , -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
        return res

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer[i] == sum(nums) - nums[i]
        # O(n)

        # 1 2 3 4
        # 24 12 8 6
        # 2 * 3 * 4 = 24 % 1 = 24
        # 1 * 3 * 4 = 24 % 2 = 12
        # 1 * 2 * 4 = 24 % 3 = 8
        # 1 * 2 * 3 = 24 % 4 = 6
        
        # 1 .get all multiple num
        # loop one by one and divide by index num
        # total = 1
        # for n in nums:
        #     total *= n

        # answer = []
        # for i, n in enumerate(nums):
        #     # cannot resolve by this case..
        #     if n == 0:
        #         temp = 
        #     else:
        #         temp = int(total / n)
        #     answer.append(temp)
        # return answer