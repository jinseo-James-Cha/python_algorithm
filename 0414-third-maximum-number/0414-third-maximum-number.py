from collections import deque
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if len(s) == 3 and num not in s:
                min_in_set = min(s)
                if min_in_set < num:
                    s.remove(min_in_set)
                    s.add(num)
            elif len(s) < 3:
                s.add(num)
        return min(s) if len(s) == 3 else max(s)

