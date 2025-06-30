from math import inf

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ### Problem
        # distict integer
        # pair of minimum absolute difference
        # return minimum difference's pairs
        
        ### Approaching
        # should I need sort?
        # abs difference
        # -14 4 -> 10
        # [3,8,-10,23,19,-4,-14,27] -> -14 -10 -4 3 8 19 23 27
        # I think sort asc and then compare only adjacent nums
        # we need to save minimum different and its array
        minimum_diff = inf
        res = []
        arr.sort()
        for i in range(len(arr) - 1):
            # skip greater diff
            if abs(arr[i] - arr[i+1]) > minimum_diff:
                continue
            # same diff
            elif abs(arr[i] - arr[i+1]) == minimum_diff:
                res.append([arr[i], arr[i+1]])
            # less than diff
            else:
                minimum_diff = abs(arr[i] - arr[i+1])
                res = [[arr[i], arr[i+1]]]
        return res