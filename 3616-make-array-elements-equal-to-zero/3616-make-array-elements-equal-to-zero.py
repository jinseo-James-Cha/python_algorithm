class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums) # 5
        ans = 0
        total_sum = sum(nums) # 6

        left, right = 0, total_sum # 0, 6
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i] # 3
                right -= nums[i] # 3
        return ans