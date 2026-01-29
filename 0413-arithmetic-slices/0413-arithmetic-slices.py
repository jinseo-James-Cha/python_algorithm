class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # consists of at least three elements
        # and the difference between any two consecutive element is the same

        """
        1 2 3 4

        len 3
        1 2 3 -> 1 between
        2 3 4 -> 1 between

        len 4
        1 2 3 4 -> 1 between



        1 2 3 5
         1 1 2
         1 1 2
         L
             R   R-L and R!= L => L = R
          
        1 2 3 4
         1 1 1
         1 1 1
         0 1 2
         L
             R    R - L + R - L = 1-0 + 2-0 => 3
        """

        if len(nums) <= 2:
            return 0
        
        diff = [0] * (len(nums)-1)
        for i in range(len(nums)-1):
            diff[i] = nums[i+1] - nums[i]
        
        # sliding window
        arithmetic_count = 0
        left = 0
        for right in range(len(diff)):
            if diff[left] == diff[right]:
                arithmetic_count += right - left
            else:
                left = right
        return arithmetic_count
