class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window 
        # 0 1 2 3 4 5 6 7 8
        # - - - -
        #   - - - -
        MODULO = 10**-5
        
        # initial with window size
        curr = sum(nums[:k])
        res = curr / k
        for i in range(k, len(nums)): # i 4 5 6 7
            curr = curr - nums[i-k] + nums[i]
            res = max(curr/k, res)
        return res
        