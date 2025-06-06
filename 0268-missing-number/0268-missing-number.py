class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)













        # answer = 0
        # for i in range(len(nums)):
        #     answer += i - nums[i]
        # return answer + len(nums)