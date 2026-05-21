class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        4 3 2 6

        F(0) = 0*4 + 1*3 + 2*2 + 3*6
        F(1) = F(0) + numSum(this is adding all numbers * 1) like 1*3 -> 2*3
                and then need to deduct the last one, which is 3*6 + 6(this is from numSum)
        so, 
        F(1) = F(0) + add all numbers each - ((n-1) * nums[n-1] - nums[n-1])
        F(1) = F(0) + numSum - ((n) * nums[n-1])
        F(n) = prev result + add all elements once - deduct the last element two times

        F(0) = 0×nums[0] + 1×nums[1] +… + (n−1)×nums[n−1]
        F(1) = 1×nums[0] + 2×nums[1] +… + 0 × nums[n−1] = F(0)+numSum−n×nums[n−1]
        """
        numSum = sum(nums)
        n = len(nums)

        # initial
        curr = 0
        for i, num in enumerate(nums):
            curr += (i * num)
        
        res = curr
        for i in range(n - 1, 0, -1):
            curr = curr + numSum - n * nums[i]
            res = max(res, curr)
        return res
