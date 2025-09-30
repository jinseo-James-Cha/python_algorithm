class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # order by red while blue
        #           0   1     2
        # just sort by ascending order
        # selection sort
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
            
        