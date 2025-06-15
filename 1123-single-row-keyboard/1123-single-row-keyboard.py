class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        kMap = {}
        for i,k in enumerate(keyboard):
            kMap[k] = i
        
        res = 0
        prev = 0
        for w in word:
            res += abs(prev - kMap[w])
            prev = kMap[w]
        return res

        