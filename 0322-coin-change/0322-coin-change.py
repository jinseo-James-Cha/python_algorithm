class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp: top-down
        def dp(coins: List[int], target: int, memo: Dict[int, int]):
            # base case
            if target == 0:
                return 0
            if target in memo:
                return memo[target]
            
            min_coins = float(inf)
            for coin in coins:
                if coin <= target:
                    min_coins = min(min_coins, 1 + dp(coins, target - coin, memo))
            
            memo[target] = min_coins
            return memo[target]

        res = dp(coins, amount, {})
        return -1 if res == float(inf) else res

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
