class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = prev = 0
        
        for num in nums:
            if num == 0:
                prev += 1
                res += prev
            else:
                prev = 0
        return res