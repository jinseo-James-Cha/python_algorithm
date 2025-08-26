class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # n : num of dice
        # k : num of face -> 1~k
        # 10**9 + 7 < answer -> 10**9 + 7


        # dp
        # possible ways

        # state
        # n, current_target
        
        # top down
        def dp(dices, current_target):
            if current_target == 0 and dices == 0:
                return 1
            
            if current_target < 0:
                return 0
            
            if dices == 0:
                return 0
            
            if (dices, current_target) not in memo:
                ways = 0
                for f in range(1, min(k, current_target) +1):
                    ways = (ways + dp(dices-1, current_target-f)) % (10**9 + 7)
                memo[(dices, current_target)] = ways 
            return memo[(dices, current_target)]

        memo = {}
        return dp(n, target)
