# Two pointers...
# [1,8,6,2,5,4,8,3,7]
# use inward ? and check left or right to move to make greater output?
# uh? min(height[left], height[right]) * (right - left) = 49

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0
        while left < right:
            h = min(height[left], height[right]) * (right - left) 
            m = max(m, h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m
        