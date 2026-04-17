class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        starting first index  = 0
        2     3    1    1    4
        start                end
        -> I can jump up to curr[index] = current to 0+2

        I don't need end number then. it needs when I need to jump?

        2 3 1 1 4
        0 1 2 3 4
                here
                curr_position
              prev_index + nums[prev_index] = curr_index
              3 + 1 = 4 YES -> curr_position -> prev_index
            prev_index + nums[prev_index] = curr_index
            2 + num[1] >= 3 => YES -> curr_position = prev_indx = 2
        """
       # brute force
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False
        reachable = [False] * n
        reachable[0] = True

        for i in range(n):# i = 0 , i = 1
            if reachable[i] == False:
                return False
            can_jump = nums[i] # 2 # 3
            for j in range(i+1, min(n, i+can_jump+1)): # 1 ~ min(5, 2+1) 1~3/// 2 ~ 5,3+1
                reachable[j] = True

        print(reachable)
        return reachable[n-1]
        
