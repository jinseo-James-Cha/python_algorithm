from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Version 3
        # (k + i) % len = the index
        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[(k+i) % len(nums)] = nums[i]
        
        for j in range(len(temp)):
            nums[j] = temp[j]
        
        # Version 2 deque
        # Using [:] change original value in-place
        # rotate() => pop() + appendleft
        # dq = deque(nums)
        # dq.rotate(k)
        # nums[:] = list(dq)
        
        # Version 1 deque
        # Using [:] change original value in-place
        # dq = deque(nums)
        # for _ in range(k):
            # temp = dq.pop()
            # dq.appendleft(temp)
        # nums[:] = list(dq)
        
        
        
        
        