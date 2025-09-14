class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        

        # left half and right half by the most highest bar ?
        highest_bar_num = height[0]
        highest_bar_index = 0
        for i, num in enumerate(height):
            if num > highest_bar_num:
                highest_bar_num = num
                highest_bar_index = i


        res = 0
        
        # left to right till the maximum
        cur_standard = height[0]
        for i in range(1, highest_bar_index):
            if cur_standard > height[i]:
                res += cur_standard - height[i]
            else:
                cur_standard = height[i]
        
        # right to the left till the maximum
        cur_standard = height[n-1]
        for j in range(n-1, highest_bar_index, -1):
            if cur_standard > height[j]:
                res += cur_standard - height[j]
            else:
                cur_standard = height[j]
        
        return res