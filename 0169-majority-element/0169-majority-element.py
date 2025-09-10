class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # space O(1)?
        count_map = {}
        max_count = 0
        res = 0

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if max_count < count_map[num]:
                max_count = count_map[num]
                res = num
        
        return res

