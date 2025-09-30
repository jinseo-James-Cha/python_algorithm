class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # order by red while blue
        #           0   1     2
        
        # one pass - two(three pointers) pointers
        left = curr = 0
        right = len(nums) - 1
        while curr <= right:
            if nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            elif nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
            curr += 1    



        
        
        # just sort by ascending order
        # selection sort
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
            
        