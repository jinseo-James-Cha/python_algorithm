class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        # return 0 for odd minimum / 1 for even minimum
        # get minimum first
        # and add by % 10 ?


        minimum = min(nums)
        
        res = 0
        while minimum > 0:
            remainder = minimum % 10 # 33 -> 3
            res += remainder
            minimum //= 10 # --> 33 // 10 -> 3

        return (int)(res % 2 == 0)