class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        maximize profit with k transactions
        buy + sell => 1 transaction
        """
        # DP bottom up
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
        for day in range(n-1, -1, -1):
            for transaction in range(k, 0, -1):
                for is_hold in range(2):
                    do_nothing = dp[day+1][transaction][is_hold]
                    do_something = 0
                    if is_hold:
                        do_something = dp[day+1][transaction-1][0] + prices[day]
                    else:
                        do_something = dp[day+1][transaction][1] - prices[day]
                    dp[day][transaction][is_hold] = max(do_nothing, do_something)

        return dp[0][k][0]

        # DP top down
        def dp(day, is_hold, transactions):
            if transactions == 0:
                return 0
            if day >= len(prices):
                return 0

            if (day, is_hold, transactions) not in memo:
                do_nothing = dp(day+1, is_hold, transactions)
                do_something = 0
                if is_hold:
                    do_something = dp(day+1, False, transactions-1) + prices[day]
                else:
                    do_something = dp(day+1, True, transactions) - prices[day]
                memo[(day, is_hold, transactions)] = max(do_nothing, do_something)
            return memo[(day, is_hold, transactions)]
        memo = {}
        return dp(0, False, k)

        # state 
        # - which day -> i
        # - transaction number -> k
        # - action -> buy or sell or nothing
        
        # bottom up 3D
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
        # dp[n][k][buying]

        for i in range(n-1, -1, -1):
            for transaction_remaining in range(1, k+1):
                for holding in range(2):
                    doNothing = dp[i+1][transaction_remaining][holding]
                    if holding:
                        doSomething = prices[i] + dp[i + 1][transaction_remaining - 1][0]
                    else:
                        doSomething = -prices[i] + dp[i + 1][transaction_remaining][1]
                    dp[i][transaction_remaining][holding] = max(doNothing, doSomething)
        
        return dp[0][k][0]


        # top down
        def dp(i, transactionTime, holdingStock):
            # two base cases
            if i == len(prices):
                return 0
            if transactionTime == k:
                return 0
            
            if (i, transactionTime, holdingStock) not in memo:
                doNothing = dp(i+1, transactionTime, holdingStock)
                doSomething = 0
                # can sell if holding a stock
                if holdingStock:
                    doSomething = prices[i] + dp(i+1, transactionTime + 1, False)
                else:
                    doSomething = -prices[i] + dp(i+1, transactionTime, True)
                memo[(i, transactionTime, holdingStock)] = max(doNothing, doSomething)

            
            return memo[(i, transactionTime, holdingStock)]

        memo = {}
        return dp(0, 0, False)
                
            

