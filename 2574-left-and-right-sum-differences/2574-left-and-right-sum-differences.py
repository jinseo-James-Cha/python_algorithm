class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """
        nums = [ 10, 4, 8, 3]

        leftsum = [0, 10, 14, 22]
        rightsum = [15, 11, 3, 0]
        answer = |15-0|, |11-10|, |14 - 3|, |22-0|

        first element is always the sum of rightsum
        last element is always the sum of leftsum

        total sum = 25
        25-10, , ,25-3

        index = 0
        => sum[..0] - totalsum - nums[0]
        => 0 - 25-10

        index = 1
        => |10 - 11|
        => |(0+10) - (3 + 8)|

        index = 2
        => 14 - 3
        => 0+10+4 - 3

        So..
        nums = [ 10, 4, 8, 3]
        leftSum = 0 -> 15
        rightsum = 25
        res = [0] * n [15, ]
        for i in range(n):
            rightnum -= nums[i] 25-10 -> 15-4
            res[i] = |leftsum - rightsum|  -> |0 - 15| => 15
            leftsum += nums[i]             -> 0 + 10 => 10
        """
        n = len(nums)

        leftSum = 0
        rightSum = sum(nums)
        res = [0] * n
        for i in range(n):
            rightSum -= nums[i] # 25 - 10
            res[i] = abs(leftSum - rightSum) # 0-15
            leftSum += nums[i] # 0 -> 10
        return res
