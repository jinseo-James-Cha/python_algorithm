class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1 ,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        d_roman = {'IV': -2, 'IX' : -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}

        answer = 0
        for a in s:
            answer += roman[a]
        
        for d in d_roman:
            if d in s:
                answer += d_roman[d]

        return answer

        