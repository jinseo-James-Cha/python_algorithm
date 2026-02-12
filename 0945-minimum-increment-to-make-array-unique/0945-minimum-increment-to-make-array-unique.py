class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 1 2 2
        # 1 2 3 -> 1

        # 3 2 1 2 1 7
        # 1 1 2 2 3 7
        # 1 2 3 4 5 7 -> 1+1+2+2
        # 1 1->4 2 2->5 3 7

        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                target = nums[i-1] + 1
                res += target - nums[i]
                nums[i] = target
        return res