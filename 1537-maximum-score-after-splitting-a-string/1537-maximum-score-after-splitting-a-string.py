class Solution:
    def maxScore(self, s: str) -> int:
        # feel like sliding window
        
        # initial window
        left = s[0]
        right = s[1:]
        max_score = -1
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            
            left_score = left.count("0")
            right_score = right.count("1")
            max_score = max(left_score+right_score, max_score)
        return max_score