class Solution:
    def removeDuplicates(self, nums: List[int]):
        res = 0
        n = len(nums)
        insert_i = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_i] = nums[i]
                insert_i += 1
        return insert_i
