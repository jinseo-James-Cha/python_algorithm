class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Follow up: 
        # Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
        checked = [False] * (len(nums) + 1)
        for n in nums:
            checked[n] = True
        
        res = len(nums)
        for i, c in enumerate(checked):
            if c == False:
                res = i
        return res


        # v1
        # time: O(n log n)
        # space: O(n)
        # nums.sort()
        # res = len(nums)
        # for i, num in enumerate(nums):
        #     if i != num:
        #         res = i
        #         break
        # return res
