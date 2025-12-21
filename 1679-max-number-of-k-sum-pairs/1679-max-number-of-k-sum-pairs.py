class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort the num and two pointer and move -=1 +=1 when it matches


        res = 0
        left = 0
        right = len(nums) - 1

        nums.sort() # O(log n)
        while left < right: # O(n)
            if nums[left] + nums[right] == k:
                res += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return res