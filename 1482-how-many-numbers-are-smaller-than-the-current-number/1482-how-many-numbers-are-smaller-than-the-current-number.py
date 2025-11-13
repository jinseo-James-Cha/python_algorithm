class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # count the number of elements having more than nums[i]
        # 8 1 2 2 3
        # 4 0 1 1 3
        res = [0] * len(nums)
        for i in range(len(nums)):
            curr_num = nums[i]
            count = 0
            for j in range(len(nums)):
                if i != j and curr_num > nums[j]:
                    count += 1
            res[i] = count
        return res