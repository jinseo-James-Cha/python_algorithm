class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        got_last_word = False
        for right in range(len(s)-1, -1, -1):
            if s[right] != " ":
                res += 1
                got_last_word = True
            elif got_last_word:
                    break
        return res
            
