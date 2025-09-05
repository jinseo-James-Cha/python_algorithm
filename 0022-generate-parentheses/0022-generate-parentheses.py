from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtrack
        def backtrack(curr, left_count, right_count):
            if len(curr) == 2*n:
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


        # BFS
        def isValid(s):
            left_count = 0
            for letter in s:
                if letter == "(":
                    left_count += 1
                else:
                    left_count -= 1
                
                if left_count < 0:
                    return False
            return left_count == 0

        res = []
        queue = deque([""])
        while queue:
            cur_string = queue.popleft()

            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    res.append(cur_string)
                continue
            
            queue.append(cur_string + "(")
            queue.append(cur_string + ")")
        return res