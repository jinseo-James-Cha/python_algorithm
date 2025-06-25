class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end
        intervals.sort(key = lambda x: x[1])
        ans = 0
        k = -inf

        for start, end in intervals:
            if start >= k: # if new start is greater than prev end
                k = end
            else:
                ans += 1
        return ans