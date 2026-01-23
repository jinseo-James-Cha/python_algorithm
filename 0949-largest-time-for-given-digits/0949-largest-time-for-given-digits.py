class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def backtrack(curr, used_idx):
            nonlocal max_time
            if len(curr) == 4:
                # validate time
                hh, mm = curr[0]+curr[1], curr[2]+curr[3]
                if 0 <= int(hh) <= 23 and 0 <= int(mm) <= 59:
                    current_time_str = hh + ":" + mm
                    max_time = max(max_time, current_time_str)
            
            for i in range(len(arr)):
                if i not in used_idx:
                    curr.append(str(arr[i]))
                    used_idx.add(i)
                    
                    backtrack(curr, used_idx)
                    
                    curr.pop()
                    used_idx.remove(i)
                    
        max_time = ""
        backtrack([], set())
        return max_time