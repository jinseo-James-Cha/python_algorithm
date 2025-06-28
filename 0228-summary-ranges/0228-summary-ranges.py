class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        # two pointer
        # 0 1 2 4 5 7
        # L
        # R R R
        #       L
        #       R R
        #           L
        #           R

        # 0 <= nums.length <= 20
        if not nums:
            return res

        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if start != nums[i]:
                res.append(str(start) + "->" + str(nums[i]))
            else:
                res.append(str(nums[i]))
            i += 1
        return res
            