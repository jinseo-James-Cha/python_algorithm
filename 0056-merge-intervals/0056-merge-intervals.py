class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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

        