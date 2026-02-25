class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr_list, curr_left, start):
            if curr_left < 0:
                return
            elif curr_left == 0:
                res.append(curr_list[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                        continue
                if curr_left < candidates[i]:
                    break
                curr_list.append(candidates[i])
                backtrack(curr_list, curr_left - candidates[i], i + 1)
                curr_list.pop()
        
        res = []
        candidates.sort()
        backtrack([], target, 0)
        return res