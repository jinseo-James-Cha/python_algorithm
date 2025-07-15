class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination_index = len(nums) - 1

        for i in range(destination_index - 1, -1, -1):
            if i + nums[i] >= destination_index:
                destination_index = i
        
        return destination_index == 0