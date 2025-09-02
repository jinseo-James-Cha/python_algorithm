class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bottom up
        def merge(left_list, right_list):
            left_index, right_index = 0,0
            merged_list = []
            while left_index < len(left_list) and right_index < len(right_list):
                if left_list[left_index] >= right_list[right_index]:
                    merged_list.append(right_list[right_index])
                    right_index += 1
                else:
                    merged_list.append(left_list[left_index])
                    left_index += 1
            merged_list.extend(left_list[left_index:])
            merged_list.extend(right_list[right_index:])
            
            return merged_list

        n = len(nums)
        width = 1
        while width < n:
            new_nums = []
            for i in range(0, n, 2 * width):
                left = nums[i:i+width]
                right = nums[i+width:i+2*width]
                new_nums.extend(merge(left, right))
            nums = new_nums
            width *= 2
        return nums



        # top down
        def merge(left_list, right_list):
            left_index, right_index = 0,0
            merged_list = []
            while left_index < len(left_list) and right_index < len(right_list):
                if left_list[left_index] >= right_list[right_index]:
                    merged_list.append(right_list[right_index])
                    right_index += 1
                else:
                    merged_list.append(left_list[left_index])
                    left_index += 1
            merged_list.extend(left_list[left_index:])
            merged_list.extend(right_list[right_index:])
            
            return merged_list


        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])
        return merge(left_list, right_list)

