class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # space O(1)?
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate




        # works, but not ok
        count_map = {}
        max_count = 0
        res = 0

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if max_count < count_map[num]:
                max_count = count_map[num]
                res = num
        
        return res

