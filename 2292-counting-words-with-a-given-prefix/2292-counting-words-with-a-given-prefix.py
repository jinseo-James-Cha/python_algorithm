class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # return num of strings in words that contain pref as a prefix
        count = 0
        pref_len = len(pref)
        for w in words:
            if len(w) >= pref_len:
                if w[:pref_len] == pref:
                    count += 1
        return count
            
        