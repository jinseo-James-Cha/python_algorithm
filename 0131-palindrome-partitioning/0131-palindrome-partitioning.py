class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(p):
            return p == p[::-1]

        def backtrack(curr_s, curr_combination):
            if not curr_s:
                res.append(curr_combination[:])
                return
            
            for i in range(1, len(curr_s) + 1):
                if is_palindrome(curr_s[:i]):
                    backtrack(curr_s[i:], curr_combination + [curr_s[:i]])

        res = []
        backtrack(s, [])
        return res
