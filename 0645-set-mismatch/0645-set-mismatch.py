class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        num_set = set(list(range(1, len(nums)+1)))
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                res[0] = num
        
        for loss in num_set:
            res[1] = loss
        return res