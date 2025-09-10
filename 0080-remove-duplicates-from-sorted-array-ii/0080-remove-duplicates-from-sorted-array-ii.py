from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        insert_index = 0
        count_map = defaultdict(int)
        
        for i, num in enumerate(nums): 
            if count_map[num] < 2: # 0 < 2
                count_map[num] += 1 # [1] = 1 -> 2
                nums[insert_index] = num # nums[0] = 1 -> nums[1] = 1
                insert_index += 1 # 1 -> 2

        return insert_index