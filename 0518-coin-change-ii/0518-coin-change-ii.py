class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # state
        # ith coins
        # amount

        # no duplication combinations !

        # bottom up optimization
        dp = [0] * (amount + 1)
        dp[0] = 1  # 0원을 만드는 방법은 아무것도 안 쓰는 경우 1개

        for c in coins:  # 코인을 바깥 루프로
            for j in range(c, amount + 1):  # j-c가 존재할 때만
                dp[j] += dp[j - c]

        return dp[amount]

        # bottom up
        n = len(coins)
        # dp[coins][amount]
        dp = [[0] * (amount + 1) for _ in range(n+1)] 
        for i in range(n):
            dp[i][0] = 1 

        for i in range(n-1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]
                    
        return dp[0][amount]




        # top down
        def dp(i, target_amount):
            if target_amount == 0:
                return 1
            if i == len(coins) or target_amount < 0:
                return 0
            
            if (i, target_amount) not in memo:
                used = dp(i, target_amount - coins[i])
                not_used = dp(i+1, target_amount)

                memo[(i,target_amount)] = used + not_used
            
            return memo[(i,target_amount)]
        
        memo = {}
        return dp(0, amount)








        # top down
        def dfs(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]
            
            if coins[i] > amount: # coin is greater than amount, skip to the next
                memo[i][amount] = dfs(i+1, amount)
            else: # calculatable coin !
                memo[i][amount] = dfs(i, amount-coins[i]) + dfs(i+1, amount)

            return memo[i][amount]
        
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        dfs(0, amount)
        print(memo)
        return 0

        # dp = [0] * (amount + 1)
        # dp[0] = 1

        # for c in coins:
        #     for a in range(1, amount + 1):
        #         if a - c >= 0:
        #             dp[a] += dp[a-c]
        # return dp[-1]
