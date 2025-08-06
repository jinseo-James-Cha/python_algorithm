class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) time ? binary search ?!
        # sorted.. log n -> BS

        # rotated 1~n times
        # 0 1 2 3 4 5 6 7
        # 4 5 6 7 0 1 2 3
        # unique elements
        # return minimum element in this array


        # brute force
        # O(n)
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                res = nums[i]
                break
        return res