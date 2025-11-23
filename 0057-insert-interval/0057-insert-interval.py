class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e, -1))

        s0, e0 = newInterval
        events.append((s0, 1))
        events.append((e0, -1))

        events.sort(key=lambda x: (x[0], -x[1]))

        res = []
        active = 0
        cur_start = None
        for t, val in events:
            prev_active = active
            active += val

            if prev_active == 0 and active > 0:
                cur_start = t

            if prev_active > 0 and active == 0:
                res.append([cur_start, t])
                cur_start = None
        return res
