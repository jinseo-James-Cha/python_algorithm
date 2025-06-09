class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                # val can be only 0 ~ 100
                nums[i] = -1

        # two pointer -> move all -1 into back
        res = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] != -1:
                nums[left], nums[right] = nums[right], nums[left]
                res += 1
                left += 1

        return res




        