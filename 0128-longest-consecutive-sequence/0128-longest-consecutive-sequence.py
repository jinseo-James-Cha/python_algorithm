class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # intuition
        # how to make consecutive...
        # O(n)
        nums_set = set(nums)
        longest_sequence = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                longest_sequence = max(longest_sequence, current_streak)
        return longest_sequence
