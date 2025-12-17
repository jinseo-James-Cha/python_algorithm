class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # abc
        # 012
        # pqr
        # 012
        # abcpqr
        # 012345
        res = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            res += word1[min_len:]
        elif len(word1) < len(word2):
            res += word2[min_len:]
        return res