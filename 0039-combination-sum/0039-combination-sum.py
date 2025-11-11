class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return a list of all unique combination?! -> backtrack
        def backtrack(start, curr, remainder):
            if 0 > remainder:
                return
            
            if remainder == 0:
                res.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, remainder - candidates[i])
                curr.pop()
            
        res = []
        backtrack(0, [], target)
        return res
