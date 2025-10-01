from math import inf

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. sort arr by counting sort
        # 2. find minimum abs val
        # 3. add a pair if its minimum val

        min_num = min(arr)
        max_num = max(arr)
        count = [0] *(max_num - min_num + 1)
        for num in arr:
            count[num - min_num] += 1
        
        # accumulated count
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        sorted_arr = [0] * len(arr)
        for num in reversed(arr):
            sorted_arr[count[num - min_num] - 1] = num
        
        # find minimum absolute difference and save pairs
        minimum_abs_diff = float('inf')
        res = []
        for i in range(len(sorted_arr) - 1):
            curr_diff = abs(sorted_arr[i] - sorted_arr[i+1])
            if minimum_abs_diff == curr_diff:
                res.append([sorted_arr[i], sorted_arr[i+1]])
            elif minimum_abs_diff > curr_diff:
                minimum_abs_diff = curr_diff
                res = [[sorted_arr[i], sorted_arr[i+1]]]
        return res
    
    








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