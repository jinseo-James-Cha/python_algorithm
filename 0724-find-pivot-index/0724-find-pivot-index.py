class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # calculate the pivot index

        # pivot index ==> sum(nums[:pivot_index]) == sum(nums[pivot_index+1:])
        # return leftmost index.. if failed, return -1


        # [1,7,3,6,5,6]
        # -> 1 8 11 17 22 28
        # -> left - right = 0
        # left = right
        # total - left = right

        # [1, 2, 3]
        #  1  3   6
        #  6  5   3

        # total - curr_prefix_sum - curr_num = curr_prefix_sum
        # total - curr_prefix_sum - curr_index_num = curr_prefix_sum
        # 28 - 11 - 6 = 11
        total = sum(nums)
        curr_prefix_sum = 0
        for i, num in enumerate(nums):
            if total - curr_prefix_sum - num == curr_prefix_sum:
                return i 
            
            curr_prefix_sum += num
        return -1




        return -1