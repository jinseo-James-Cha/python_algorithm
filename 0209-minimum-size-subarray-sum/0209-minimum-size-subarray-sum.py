class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        subarray sum >= target -> and return its minimum size 
        sum(i ~ j) >= target

        assumption
        num > 0 -> edge case -> sum(all) < target -> no answer
                             -> if target == 1: return 1

        brute force
        - check all subarray with nested loops -> o(n^2)
        - sum the current subarray and check with target O(n)
        => o(n^3)

        two pointers
        - add until subarray >= target and check length by right pointer - left pointer + 1
        - does it work even though it is not sorted? I think so
        - o(n)
        """
        if target > sum(nums):
            return 0
        if target == sum(nums):
            return len(nums)
        if target == 1:
            return 1

        minimum_size = float('inf')
        curr_total_sum = 0
        left = 0
        for right in range(len(nums)):
            curr_total_sum += nums[right]
            while curr_total_sum >= target: # 8 >= 7 -> 
                minimum_size = min(minimum_size, right - left + 1)
                
                curr_total_sum -= nums[left] # 8 -> 6
                left += 1 # 1

        return minimum_size if minimum_size != float('inf') else 0
        