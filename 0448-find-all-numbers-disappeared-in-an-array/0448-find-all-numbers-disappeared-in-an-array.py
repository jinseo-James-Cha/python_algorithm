class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # brute force
        num_set = set(list(range(1, len(nums) + 1)))
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        
        return list(num_set)
        
        # without extra space
        # O(n) runtime