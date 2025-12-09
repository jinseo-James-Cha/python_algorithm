class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices one pair and not the same index

        res = [0, 0]
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                res = [hashmap[target-num], i]
            else:
                hashmap[num] = i
        return res