class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # all combinations -> backtrack ?
        def backtrack(curr, left, right):
            # base case
            if left + right == n*2:
                res.append("".join(curr))
                return
            
            if left < n:
                curr.append('(')
                backtrack(curr, left+1, right)
                curr.pop()
            
            if right < n and right < left:
                curr.append(')')
                backtrack(curr, left, right + 1)
                curr.pop()

        res = []
        backtrack([], 0, 0)
        return res
            

