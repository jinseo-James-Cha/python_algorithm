class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # backtrack for all subset
        res = 0
        
        def backtrack(start, current_xor):
            nonlocal res
            res += current_xor
            for i in range(start, len(nums)):
                backtrack(i+1, current_xor ^ nums[i])
        
        backtrack(0, 0)
        return res