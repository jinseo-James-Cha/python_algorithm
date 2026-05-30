"""
Problem description
Given an array height[], where each element represents the height of a vertical line at index i, the container’s area is limited by the shorter of two chosen lines and the distance between them:
Area = min(height[i], height[j]) × (j − i).
The goal is to select i and j to maximize this product.

For example, for height = [1,8,6,2,5,4,8,3,7], the optimal container uses heights 8 and 7, yielding area 49.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:

        

		#check this




        max_water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, w*h)

            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return max_water