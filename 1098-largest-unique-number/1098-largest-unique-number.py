class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # once and largest
        # or return -1 if there

        # sort desc and check
        if len(nums) == 1:
            return nums[0]
        

        # nums 0 ~ 1000
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        
        print(count)

        res = -1
        for i in range(len(count)-1, -1, -1):
            if count[i] == 1:
                res = i
                break
        return res