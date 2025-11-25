class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 1 0 1 == 5
        # 1 1 0 == 6
        # 1 1 1 == 7
        
        while left < right:
            right = right & (right - 1)
        return right

