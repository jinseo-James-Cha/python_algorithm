class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:

        res = []


        def backtrack(start, remainder, combination):
            if remainder == 0:
                res.append(combination[:])
                return
            elif remainder < 0:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, remainder - candidates[i], combination)
                combination.pop()

        backtrack(0, target, [])
        return res