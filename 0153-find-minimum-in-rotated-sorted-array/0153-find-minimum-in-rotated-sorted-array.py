class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) time ? binary search ?!
        # sorted.. log n -> BS

        # rotated 1~n times
        # 0 1 2 3 4 5 6 7
        # 4 5 6 7 0 1 2 3
        # unique elements
        # return minimum element in this array
        if len(nums) == 1:
            return nums[0]
        
        if nums[-1] > nums[0]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1



        # brute force
        # O(n)
        # res = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         res = nums[i]
        #         break
        # return res