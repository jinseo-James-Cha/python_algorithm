# 3 <= nums.length <= 100
# 1 <= nums[i] <= 106

# Brute Force -> O(n^3) 

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = -1
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if m < (nums[i] - nums[j]) * nums[k]:
                        m = (nums[i] - nums[j]) * nums[k]

        return m if m > 0 else 0

        