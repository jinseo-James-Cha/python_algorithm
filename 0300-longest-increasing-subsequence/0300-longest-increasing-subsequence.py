from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        10 9 2 5 3 7 101 18
        -> longest -> 2 3 7 101

        monotonic stack?

        10
        9
        2 5 and 3 is smaller than 5 -> pop() -> and append -> 2 3
        7 is greater 3 => 2 3 7
        101 is greater 7 => 2 3 7 101
        18 is smaller than 101 -> but 2 3 7 18 possible
        """

        stack = []
        longest = 0
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                if stack[-1] < num:
                    stack.append(num)
                else:
                    insert_idx = bisect_left(stack, num)
                    stack[insert_idx] = num
        return len(stack)
