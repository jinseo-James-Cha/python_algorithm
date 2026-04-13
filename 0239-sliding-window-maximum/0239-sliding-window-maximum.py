from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,3,-1,-3,5, 3], k = 3
        # monotonic deque
        queue = deque()
        maximums = []
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        maximums.append(nums[queue[0]])

        for i in range(k, len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()
            
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()

            queue.append(i)
            maximums.append(nums[queue[0]]) 

        return maximums



        # deque
        # O(n * k)
        pq = deque(nums[:k])
        maximums = []
        maximums.append(max(pq))
        for i in range(k, len(nums)):
            pq.popleft()
            pq.append(nums[i])
            maximums.append(max(pq))
        return maximums

        # brute force
        # o(n * k) -> TLE
        if k == 1:
            return nums
        max_nums_in_sliding_window = []
        window = nums[:k]
        max_nums_in_sliding_window.append(max(nums[:k]))

        left = 1
        for right in range(k, len(nums)):  
            curr_window = nums[left: right+1]
            max_nums_in_sliding_window.append(max(curr_window))
            left += 1
        return max_nums_in_sliding_window