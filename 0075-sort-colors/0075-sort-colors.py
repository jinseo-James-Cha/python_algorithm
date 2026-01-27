class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1

        curr_idx = 0
        for color in range(3):
            for _ in range(colors[color]):
                nums[curr_idx] = color
                curr_idx += 1

        # red_idx = 0
        # blue_idx = len(nums)-1
        # curr_idx = 0
        # while curr_idx <= blue_idx:
        #     if nums[curr_idx] == 0:
        #         nums[red_idx], nums[curr_idx] = nums[curr_idx], nums[red_idx]
        #         red_idx += 1
        #         curr_idx += 1
        #     elif nums[curr_idx] == 2:
        #         nums[blue_idx], nums[curr_idx] = nums[curr_idx], nums[blue_idx]
        #         blue_idx -= 1
        #     else:
        #         curr_idx += 1

        


        # # counting sort
        # count = [0, 0, 0]
        # for num in nums:
        #     count[num] += 1
        
        # curr_index = 0
        # for i in range(3): # 0, 1, 2
        #     for _ in range(count[i]):
        #         nums[curr_index] = i
        #         curr_index += 1


        # # order by red while blue
        # #           0   1     2
        
        # # one pass - two(three pointers) pointers
        # left, curr, right = 0, 0, len(nums) - 1
        # while curr <= right:
        #     if nums[curr] == 2:
        #         nums[curr], nums[right] = nums[right], nums[curr]
        #         right -= 1
        #     elif nums[curr] == 0:
        #         nums[left], nums[curr] = nums[curr], nums[left]
        #         left += 1
        #         curr += 1
        #     else:
        #         curr += 1    



        
        
        # # just sort by ascending order
        # # selection sort
        # for i in range(len(nums)):
        #     min_index = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     nums[i], nums[min_index] = nums[min_index], nums[i]
            
        