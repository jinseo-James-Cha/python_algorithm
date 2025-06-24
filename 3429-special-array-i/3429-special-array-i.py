class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # special -> odd even odd even    or      even odd even odd
        prev_check = True if nums[0] % 2 == 0 else False

        for i in range(1, len(nums)):
            if (nums[i] % 2 == 0) == prev_check:
                return False
            else:
                prev_check = not prev_check
        return True
