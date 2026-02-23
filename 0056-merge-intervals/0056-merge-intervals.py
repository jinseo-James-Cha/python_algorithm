class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #  1 2 3 4 5 6 7 8 9 10
        #A - - -
        #B    - - - - -
        #C               - - -

        # to check intervals by start time.. 
        # case 1:
        # A.end < B.start -> Non-overlapping found
        #  append B     

        # case 2:
        # A.end >= B.start -> overlapping
        # update A.start, max(A.end, B.end)

        intervals.sort(key=lambda x:x[0])
        non_overlapping = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = non_overlapping[-1]
            curr = intervals[i]
            if prev[1] < curr[0]:
                non_overlapping.append(curr)
            else:
                non_overlapping[-1] = [prev[0], max(prev[1], curr[1])]
        
        return non_overlapping


        















        # intervals -> sweep line algorithm?
        events = []
        for start, end in intervals:
            events.append((start, -1))
            events.append((end, 1))
        
        events.sort(key=lambda x:[x[0], x[1]])

        res = []
        curr = [float('inf'), -float('inf')]
        curr_val = 0
        for num, val in events:
            curr_val += val
            if val < 0 and num < curr[0]:
                curr[0] = num
            elif val > 0 and num > curr[1]:
                curr[1] = num
            
            if curr_val == 0:
                res.append(curr)
                curr = [float('inf'), -float('inf')]
        return res

        # intervals A and B will never overlap when A.end < B.start

        # if A.end < B.start, NO OVERLAP
        # if A.end >= B.start OVERLAP

        # to sort intervals by start value
        intervals.sort(key=lambda x:x[0]) # sort by first element
        
        # initial with first interval
        merged = [intervals[0]] 
        # compare intervals
        for B in intervals[1:]:
            # get current(most recent) interval
            A = merged[-1] 

            # A.end < B.start is NO OVERLAP
            if A[1] < B[0]:
                # move to next overlap with B
                merged.append(B)
            else:
                # expand overlap between A and B
                merged[-1] = [A[0], max(A[1], B[1])]
        return merged

        