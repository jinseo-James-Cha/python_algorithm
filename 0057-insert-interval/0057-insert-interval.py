class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        i = 0
        is_inserted = False
        events = []
        while i < len(intervals):
            start, end = intervals[i]
            if is_inserted:
                events.append(intervals[i])
                i += 1
            else:
                new_start, new_end = newInterval
                if start < new_start:
                    events.append(intervals[i])
                    i += 1
                elif start > new_start:
                    events.append(newInterval)
                    is_inserted = True
                else:
                    if end <= new_end:
                        events.append(intervals[i])
                        i += 1
                    else:
                        events.append(newInterval)
                        is_inserted = True
        events.extend(intervals[i:])
        if len(events) == len(intervals):
            events.append(newInterval)
        
        new_events = []
        for start, end in events:
            new_events.append((start, -1))
            new_events.append((end, 1))
        
        new_events.sort()

        res = []
        curr_num = 0
        curr_list = [float('inf'), -float('inf')]
        for num, val in new_events:
            curr_num += val
            if val < 0 and curr_list[0] > num:
                curr_list[0] = num
            elif val > 0 and curr_list[1] < num:
                curr_list[1] = num

            if curr_num == 0:
                res.append(curr_list)
                curr_list = [float('inf'), -float('inf')] 
        return res

