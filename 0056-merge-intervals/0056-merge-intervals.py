class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1 2 3 4 5 6 7 8
        - - -
          - - - - -
        1~~~~~~~~~6
        """
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
        