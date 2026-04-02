class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # should I sort coins by reverse? -> yes to get the fewest number of coins
        """
        11

        5 2 1
        11 - 5 => 6 => 1 coin
        6 - 5 => 1 => 2 coins
        1 - 2 X
        1 - 1 => 0 => 3 coins

        """


        # DP - bottom up
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for target in range(coin, amount + 1):
                dp[target] = min(dp[target], dp[target - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
                

        # DP - top down
        def dp(target):
            if target == 0:
                return 0
            
            if target < 0:
                return -1
            
            fewest = float('inf')
            if target not in memo:
                for coin in coins:
                    res = dp(target - coin)
                    if res != -1:
                        fewest = min(fewest, res + 1)
                memo[target] = fewest if fewest != float('inf') else -1
            return memo[target]

        memo = {}
        return dp(amount)



        # fewest combinations.. sort by descening order? and backtrack
        # TLE
        def backtrack(curr_coins, start):
            nonlocal fewest_number
            if sum(curr_coins) == amount:
                fewest_number = min(fewest_number, len(curr_coins))
                return
            if sum(curr_coins) > amount:
                return
            
            if len(curr_coins) >= fewest_number:
                return
            
            for i in range(start, len(coins)):
                curr_coins.append(coins[i])
                backtrack(curr_coins, i)
                curr_coins.pop()

        fewest_number = float('inf')
        backtrack([], 0)
        return fewest_number if fewest_number != float('inf') else -1
        

        # bottom up
        dp = [float(inf)] * (amount+1)
        dp[0] = 0
        for target in range(1, amount+1):
            for coin in coins:
                if coin <= target:
                    dp[target] = min(dp[target], 1 + dp[target - coin])
        return dp[amount] if dp[amount] != float(inf) else -1


        # top down
        def dp (target):
            # base case
            if target < 0:
                return -1
            if target == 0:
                return 0
            
            fewest = float(inf)
            if target not in memo:
                for c in coins:
                    res = dp(target - c)
                    if res != -1:
                        fewest = min(fewest, res + 1)
                memo[target] = fewest if fewest != float(inf) else -1
            return memo[target]

        memo = {}
        return dp(amount)









        # dp: bottom-up
        # dp = [float(inf)] * (amount + 1)
        # dp[0] = 0

        # for t in range(1, amount + 1):
        #     for coin in coins:
        #         if coin <= t:
        #             dp[t] = min(dp[t], 1 + dp[t - coin])
        # return dp[amount] if dp[amount] != float(inf) else -1

        # # dp: top-down
        # def dp(coins: List[int], target: int, memo: Dict[int, int]):
        #     # base case
        #     if target == 0:
        #         return 0
        #     if target in memo:
        #         return memo[target]
            
        #     min_coins = float(inf)
        #     for coin in coins:
        #         if coin <= target:
        #             min_coins = min(min_coins, 1 + dp(coins, target - coin, memo))
            
        #     memo[target] = min_coins
        #     return memo[target]

        # res = dp(coins, amount, {})
        # return -1 if res == float(inf) else res

        # this is not working
        # if amount == 0:
        #     return 0

        # if len(coins) == 1 and coins[0] > amount:
        #     return -1

        # coins.sort(reverse=True) # to get fewer number
        # minimum = float(inf)
        # coin = 0
        # i = 0
        # current = 0
        # originalAmount = amount
        # while amount > 0 and i < len(coins): # 11
        #     if coins[i] <= amount: # 5 < 11
        #         amount -= coins[i] #  11 - 5 = 6
        #         coin += 1
        #     else:
        #         i += 1
            
        #     if amount == 0 or (amount != 0 and i == len(coins)):
        #         minimum = min(minimum, coin)
        #         current += 1
        #         i = current
        #         amount = originalAmount
        
        # if minimum == float(inf):
        #     return -1
        # else:
        #     return minimum
