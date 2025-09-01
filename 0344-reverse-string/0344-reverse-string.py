class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseByIndex(left, right):
            if left >= right:
                return
            
            s[left], s[right] = s[right], s[left]
            reverseByIndex(left + 1, right - 1)
        
        reverseByIndex(0, len(s)-1)