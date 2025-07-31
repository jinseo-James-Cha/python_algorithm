# Two pointers...
# [1,8,6,2,5,4,8,3,7]
# use inward ? and check left or right to move to make greater output?
# uh? min(height[left], height[right]) * (right - left) = 49

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # try 2
        maximum_amount = 0
        
        left = 0
        right = len(height) - 1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            current_amount = h * w
            
            maximum_amount = max(current_amount, maximum_amount)

            # move smaller line to the next
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return maximum_amount












        # left = 0
        # right = len(height) - 1
        # m = 0
        # while left < right:
        #     h = min(height[left], height[right]) * (right - left) 
        #     m = max(m, h)
        #     if height[left] < height[right]:
        #         left += 1
        #     elif height[left] = height[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         right -= 1
        # return m
        