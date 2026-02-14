class Solution:
    def makePalindrome(self, s: str) -> bool:
        # Operation -> change alphabet..
        # up to two operations..
        # means make s palindrome even though it has 2 mismatches.
        
        left = 0
        right = len(s) - 1
        mismatches = 0
        while left < right:
            if s[left] != s[right]:
                mismatches += 1
            
            left += 1
            right -= 1
        
        return mismatches <= 2