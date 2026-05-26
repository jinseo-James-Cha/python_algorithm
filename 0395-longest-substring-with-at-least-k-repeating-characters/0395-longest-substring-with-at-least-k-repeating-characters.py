from collections import Counter, defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        a a a b b
        L
        R R R count[a] >= k -> right - left + 1 => 3
              R R
        """
        
        # Divide And Conquer
        if len(s) < k:
            return 0
        
        counts = Counter(s)

        for ch, freq in counts.items():
            # no availabile character
            if freq < k:
                divides = s.split(ch)

                return max(self.longestSubstring(divide, k) for divide in divides)
        
        return len(s)