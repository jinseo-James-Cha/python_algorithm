class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        return number of combinations -> make up that amount
        """
        # DP - top down
         # top down
        def dp(i, target_amount):
            if target_amount == 0:
                return 1
            if i == len(coins) or target_amount < 0:
                return 0
            
            if (i, target_amount) not in memo:
                # possibilities
                # use the coin + not use the coin
                used = dp(i, target_amount - coins[i])
                not_used = dp(i+1, target_amount)

                memo[(i,target_amount)] = used + not_used
            return memo[(i,target_amount)]
        
        memo = {}
        return dp(0, amount)


        # brute force
        # check all combination using backtracking
        # res += 1 if amount == sum(current_combination)
        # nothung if amount < sum(current_combination)
        # combination 1 1 1 2 == 2 1 1 1, so we don't need duplications
        # using index to check only further combination.
        # TLE -> O(n^amount)
        def backtrack(curr_amount, start):
            nonlocal res
            if curr_amount < 0:
                return
            if curr_amount == 0:
                res += 1

            for i in range(start, len(coins)):
                coin = coins[i]
                if curr_amount - coin >= 0:
                    curr_amount -= coin
                    backtrack(curr_amount, i)
                    curr_amount += coin 
        res = 0
        backtrack(amount, 0)
        return res