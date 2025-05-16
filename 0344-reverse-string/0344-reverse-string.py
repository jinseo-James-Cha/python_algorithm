# my solition 1 - recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # space O(1)
        return self.reverse(s, 0, len(s) - 1)
        
    def reverse(self, s: List[str], start, end) -> List[str]:
        if end - start < 1:
            return s
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
        return self.reverse(s, start, end)
