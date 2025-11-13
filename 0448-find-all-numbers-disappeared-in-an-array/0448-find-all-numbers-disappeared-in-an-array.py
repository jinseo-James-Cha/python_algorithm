class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # without extra space
        # O(n) runtime
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1

            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        res = []
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                res.append(i)
        return res
        
        # brute force
        num_set = set(list(range(1, len(nums) + 1)))
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        
        return list(num_set)
        
        