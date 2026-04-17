from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        nums  1 3 -1 -3 5 3 6 7
        index 0 1  2  3 4 5 6 7

        window size = 3

        1 3 -1 

        3 -1 -> 3

        3 -1 -3 -> 3

        3 -1 -3 5 -> 3 valid in this window? no 
        5 -> 5

        5 3 -> 5 is valid ? yes -> 5
        6 -> 6 is biggiest -> 5 3 removed  -> 6

        6 7 -> 7 is biggiest ->6 removed -> 7
        """


        """
        1 3 -1 -3 and k = 2

        queue = [2]
        res = [1, 3, 3, -1]
        """
        n = len(nums)
        if k == 0 or n == 0:
            return [0]
        if k >= len(nums):
            return [max(nums)]

        queue = deque() #
        res = []
        for i in range(len(nums)): # 2
            if queue and i - queue[0] == k: # # 1 and 2 - 1 == k nope -> 3 - 1 == 2 yes
                queue.popleft()
            
            while queue and nums[queue[-1]] <= nums[i]: # 3 <= -1 nope
                queue.pop() # pop 0
            
            queue.append(i) # 1 2 -> 2 3

            res.append(nums[queue[0]]) # -1
        return res[k-1:]





        """
        Question
        - given integers = nums
        - size = k
         1 2 3 4
        [1 2]
           [2 3]
              [3 4]

        1.assume k size >= 0
          -> edge case k size 0 => return 0
          -> edge case k size 1 => return max(given nums)
          -> calculate length of nums - k + 1 -> 4 - 2 + 1 => 3 times 
        
        2. assume nums size >= 0
          -> edge case length == 0 => return 0
          -> edge case nums size <= k => return sum(nums)

        naive solution
        - check all windows
        - using two pointers left will deduct and right will add
        - setting up initial window by k size and loop after the size
        - update maximum sum
        """

        # edge cases
        n = len(nums)
        if n == 0 or k == 0:
            return 0
        if k == 1:
            return max(nums)
        if n <= k:
            return sum(nums)
        
        curr_window_sum = sum(nums[:k])
        max_window_sum = sum(nums[:k])

        left = 0
        for right in range(k, len(nums)):
            curr_window_sum -= nums[left]
            curr_window_sum += nums[right]
            max_window_sum = max(max_window_sum, curr_window_sum)
            
            left +=1
        return max_window_sum
            

