class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        return number of combinations -> make up that amount
        """
        # DP - top down
        def dp(curr_amount, start_idx):
            if curr_amount == 0:
                return 1
            if curr_amount < 0:
                return 0
            
            if (curr_amount, start_idx) not in memo:
                counts = 0
                for i in range(start_idx, len(coins)):
                    if curr_amount - coins[i] >= 0:
                        counts += dp(curr_amount-coins[i], i)
                memo[(curr_amount, start_idx)] = counts
            return memo[(curr_amount, start_idx)]

        memo = {}
        return dp(amount, 0)


        



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