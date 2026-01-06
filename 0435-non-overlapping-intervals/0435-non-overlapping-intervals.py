class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print(intervals)

        res = 0
        current_end = float('-inf')
        for start, end in intervals:
            if start >= current_end :
                current_end = end
            else:
                res += 1
        return res