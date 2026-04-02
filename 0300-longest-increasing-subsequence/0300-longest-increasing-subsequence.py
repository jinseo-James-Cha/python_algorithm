from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        10 9 2 5 3 7 101 18
        -> longest -> 2 3 7 101

        10
        9
        2 5 and 3 is smaller than 5 -> pop() -> and append -> 2 3
        7 is greater 3 => 2 3 7
        101 is greater 7 => 2 3 7 101
        18 is smaller than 101 -> but 2 3 7 18 possible
        """
        stack = []
        for num in nums:
            insert_idx = bisect_left(stack, num)
            if insert_idx == len(stack):
                stack.append(num)
            else:
                stack[insert_idx] = num
        return len(stack)

        # dp bottom up
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)