# 3 <= nums.length <= 100
# 1 <= nums[i] <= 106

# Brute Force -> O(n^3) -> 100 * 100^3 ? 


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        sums = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    sums.append((nums[i] - nums[j]) * nums[k])

        m = max(sums)
        return m if m > 0 else 0

        