class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        """
        1 4 2 5 3
        0 1 2 3 4

        1 4 2 5 3 -> 5
        4 -> 1
        2 5 3 -> 3
        5 -> 1
        3 -> 1
        """
        # monotonic stack
        # O(n)
        res = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                res += i - stack[-1]
                stack.pop()
            stack.append(i)

        while stack:
            res += len(nums) - stack[-1]
            stack.pop()
        return res

        # brute force 
        # time complexity -> o(n^2)
        res = 0
        for i in range(len(nums)):
            res += 1
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[i]:
                    res += 1
                else:
                    break

        return res