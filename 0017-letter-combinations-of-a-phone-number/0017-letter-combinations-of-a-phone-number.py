class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # all possible ? -> backtrack

        telephone_buttons = {}
        telephone_buttons['1'] = []
        telephone_buttons['2'] = ['a', 'b', 'c']
        telephone_buttons['3'] = ['d', 'e', 'f']
        telephone_buttons['4'] = ['g', 'h', 'i']
        telephone_buttons['5'] = ['j', 'k', 'l']
        telephone_buttons['6'] = ['m', 'n', 'o']
        telephone_buttons['7'] = ['p', 'q', 'r', 's']
        telephone_buttons['8'] = ['t', 'u', 'v']
        telephone_buttons['9'] = ['w', 'x', 'y', 'z']

        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            
            for letter in telephone_buttons[digits[i]]:
                curr.append(letter)
                backtrack(i+1, curr)
                curr.pop()
        
        res = []
        backtrack(0, [])
        return res
            
            