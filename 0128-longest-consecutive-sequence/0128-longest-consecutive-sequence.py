class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        unsorted array nums
        return the longest length which makes consecutive elements sequence
        [100, 4, 200, 1, 3, 2] -> 1 2 3 4 -> return 4
        """
        # hashset
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1  not in num_set:
                curr = num
                while curr + 1 in num_set:
                    curr += 1
                longest = max(longest, curr - num + 1)
        return longest



        # Bucket sort 
        # T.C: O(n + max(nums) - min(nums))
        # S.C: O(max(nums) - min(nums)) -> MLE
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        minimum = min(nums)
        maximum = max(nums)
        bucket = [False] * (maximum - minimum + 1)
        for num in nums:
            bucket[num - minimum] = True

        longest = 0
        for i, num in enumerate(bucket):
            if not bucket[i]:
                continue
            if i > 0 and bucket[i - 1]:
                continue
            
            curr = i
            while curr + 1 < len(bucket) and bucket[curr + 1]:
                curr += 1
            longest = max(longest, curr - i + 1)

        return longest


        # brute force -> n^2 -> TLE
        # 100 check 101...until it doesn't find the next

        if not nums:
            return 0
        longest = 1
        nums_set = set(nums)
        for num in nums:
            curr = num
            while curr + 1 in nums_set:
                curr += 1
            longest = max(longest, curr - num + 1)
        return longest