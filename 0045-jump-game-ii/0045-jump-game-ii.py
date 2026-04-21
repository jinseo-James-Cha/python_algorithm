class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        n = len(nums)

        initial position 0
        each element nums[i] -> maximum length of jump from i

        2 3 1 1 4
        F F F
          S S S S     =>  2jumps 
        
        2 3 0 1 4
        F F F
          S S S S   => 2 jumps

        when can I count a new jump?
        first max -> 1
        second max -> 1 when to switch to second jump? when there is no more jump
        """
        curr_max = 0
        next_max = 0
        jumps = 0
        for i in range(len(nums) - 1):
            next_max = max(next_max, i + nums[i])
            
            if i == curr_max:
                curr_max = next_max
                jumps += 1
        return jumps

        





        """
        dp -> O(n^2)
        2 3 1 1 4
        2 1 2 1 0
        <- <- <- <-
        """
        n = len(nums)
        jumps = [0] * n
        for i in range(n-2, -1, -1): # 5-2 3
            if nums[i] == 0:
                jumps[i] = float('inf')
                continue

            curr_jump = nums[i] 
            min_val = float('inf')
            for j in range(i+1, min(n, i + curr_jump + 1)): 
                min_val = min(min_val, jumps[j])
            
            jumps[i] = min_val + 1
        return jumps[0]

