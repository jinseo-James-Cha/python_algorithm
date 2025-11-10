class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combination questions -> backtrack ?
        # 1 ~ n and k 
        def backtrack(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(start, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        
        res = []
        backtrack(1, [])
        return res
