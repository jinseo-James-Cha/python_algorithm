class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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

