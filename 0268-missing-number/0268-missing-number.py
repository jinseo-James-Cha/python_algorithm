class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            answer += i - nums[i]
        return answer + len(nums)