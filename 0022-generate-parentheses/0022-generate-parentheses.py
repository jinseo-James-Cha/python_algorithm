class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtrack
        def backtrack(curr, left_count, right_count):
            if len(curr) == n*2:
                res.append("".join(curr))
                return
            
            if left_count < n:
                curr.append("(")
                backtrack(curr, left_count+1, right_count)
                curr.pop()
            
            if right_count < left_count:
                curr.append(")")
                backtrack(curr, left_count, right_count+1)
                curr.pop()
        
        res = []
        backtrack([], 0, 0)
        return res