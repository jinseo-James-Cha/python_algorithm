# return true for Good and false otherwise
# good means all chars has the same num of occurrences

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dct = {}
        for char in s:
            if char in dct:
                dct[char] += 1
            else:
                dct[char] = 1
        
        v_dct = list(dct.values())
        for i in range(len(v_dct) - 1):
            if not v_dct[i] == v_dct[i+1]:
                return False
        
        return True

        