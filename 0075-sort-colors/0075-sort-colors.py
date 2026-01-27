class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        
        nums[0:red] = [0] * red
        nums[red:red+white] = [1] * white
        nums[red+white:] = [2] * blue


        # counting sort
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        
        curr_index = 0
        for i in range(3): # 0, 1, 2
            for _ in range(count[i]):
                nums[curr_index] = i
                curr_index += 1


        # order by red while blue
        #           0   1     2
        
        # one pass - two(three pointers) pointers
        left, curr, right = 0, 0, len(nums) - 1
        while curr <= right:
            if nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            elif nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            else:
                curr += 1    



        
        
        # just sort by ascending order
        # selection sort
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
            
        