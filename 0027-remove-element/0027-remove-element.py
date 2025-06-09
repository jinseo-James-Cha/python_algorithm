class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                # val can be only 0 ~ 100
                nums[i] = -1

        # two pointer -> move all -1 into back
        left = 0
        for right in range(len(nums)):
            if nums[right] != -1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return left




        