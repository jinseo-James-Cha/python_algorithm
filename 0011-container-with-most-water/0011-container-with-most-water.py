class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 190
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