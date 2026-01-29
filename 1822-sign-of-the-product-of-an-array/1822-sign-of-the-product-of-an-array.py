class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        signFunc(x)
        -> 1 if x > 0
        -> -1 if x < 0
        -> 0 if x == 0
        """


        # if negative even number of - -> all positive
        # if 0 -> all 0
        # negative number odd number -> negative
        negative = 0
        for num in nums:
            if num < 0:
                negative += 1
            elif num == 0:
                return 0
        
        return 1 if negative % 2 == 0 else -1