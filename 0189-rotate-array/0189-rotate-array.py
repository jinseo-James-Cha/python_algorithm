class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1


        # i like this solution
        n = len(nums)
        k %= n

        rotate(nums, 0, n-1)
        rotate(nums, 0, k-1)
        rotate(nums, k, n-1)
