class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # all combinations .. and range smaller... -> backtracking
        letter_combinations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        def backtrack(curr_combi, start):
            if len(curr_combi) == n:
                res.append("".join(curr_combi))
                return
            
            for letter in letter_combinations[digits[start]]:
                curr_combi.append(letter)
                backtrack(curr_combi, start + 1)
                curr_combi.pop()
        
        res = []
        backtrack([], 0)
        return res
