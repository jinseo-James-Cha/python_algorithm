from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # not working cuz it is not in-place
        # nums = nums[len(nums) - k:] + nums[:len(nums) - k + 1]
            
        # deque
        # Using [:] change original value in-place
        # rotate() => pop() + appendleft
        
        dq = deque(nums)
        dq.rotate(k)
        # for _ in range(k):
            # temp = dq.pop()
            # dq.appendleft(temp)
            
        nums[:] = list(dq)