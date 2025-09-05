class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_to_letters = {}
        digits_to_letters['2'] = ['a', 'b', 'c']
        digits_to_letters['3'] = ['d', 'e', 'f']
        digits_to_letters['4'] = ['g', 'h', 'i']
        digits_to_letters['5'] = ['j', 'k', 'l']
        digits_to_letters['6'] = ['m', 'n', 'o']
        digits_to_letters['7'] = ['p', 'q', 'r', 's']
        digits_to_letters['8'] = ['t', 'u', 'v']
        digits_to_letters['9'] = ['w', 'x', 'y', 'z']

        def backtrack(curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            
            for letter in digits_to_letters[digits[len(curr)]]:
                curr.append(letter)
                backtrack(curr)
                curr.pop()
        
        res = []
        backtrack([])
        return res


