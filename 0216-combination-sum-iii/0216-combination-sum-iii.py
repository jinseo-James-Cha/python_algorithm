class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # backtrack
        res = []

        def backtrack(combination, start):
            if len(combination) == k:
                if sum(combination) == n:
                    res.append(combination[:])
                return
            
            for i in range(start, 10):
                combination.append(i)
                backtrack(combination, i + 1)
                combination.pop()
        
        backtrack([], 1)
        return res