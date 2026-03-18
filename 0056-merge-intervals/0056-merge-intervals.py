class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1 2 3 4 5 6 7 8 9 10
        - - -
          - - - - -
                      - - -
        sort
        check overlapping
        [1,3]
        if prev_end >= next's start 2 => overlapping -> until max of their end
        """
        intervals.sort()
        overlapping = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev_start, prev_end = overlapping[-1]
            curr_start, curr_end = intervals[i]
            
            if prev_end >= curr_start:
                overlapping[-1] = [prev_start, max(prev_end, curr_end)]
            else:
                overlapping.append([curr_start, curr_end])
        
        return overlapping

        # v2 sweep line
        # o(n log n)
        events = []
        for start, end in intervals:
            events.append((start, -1))
            events.append((end, 1))
        
        events.sort()
        merged = []
        curr = [float('inf'), float('-inf')]
        curr_score = 0

        for position, score in events:
            # open
            if score < 0 and curr[0] > position:
                curr[0] = position
            # close
            elif score > 0 and curr[1] < position:
                curr[1] = position
            
            curr_score += score
            if curr_score == 0:
                merged.append(curr)
                curr = [float('inf'), float('-inf')]
        return merged


        # o(n log n)
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            if prev[1] >= curr[0]:
                merged[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                merged.append(curr)
        return merged

    
        