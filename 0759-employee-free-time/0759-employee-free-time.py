"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        working time in schedule

        each schedule[i] is an employee's schedule
        
        free time
        employee 1 => [1,2], [5, 6] => free time [-inf, 1] [2, 5] [6, inf]
        employee 2 => [1,3] => free time [-inf, 1], [3, inf] => [3, 5]
        employe 3 => [4, 10] => [-inf, 4] [10, inf] => [3, 4]
        
        1. get all intervals
        2. merge intervals
        3. get gaps between end[i-1], start[i] if > 0
        """
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)

        intervals.sort(key=lambda x:x.start)

        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        
        free = []
        for i in range(1, len(merged)):
            if merged[i].start - merged[i-1].end > 0:
                free.append(Interval(merged[i-1].end, merged[i].start))
        
        return free






        events = []
        for employee in schedule:
            for interval in employee:
                events.append((interval.start, 1))
                events.append((interval.end, -1))

        events.sort()
        
        res = []
        prev = None
        curr_score = 0
        for time, score in events:
            if curr_score == 0 and prev is not None:
                if time - prev > 0:
                    res.append(Interval(prev, time))
            
            curr_score += score
            prev = time
        return res