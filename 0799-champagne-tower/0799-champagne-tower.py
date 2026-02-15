class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 1 - 1 glass
        # 2 - 2 glass
        # 3 - 3 glass
        # ...
        # 100 - 100 glass



        # 0
        # 0 0
        # 0 0 0 (2,1) -> (1,0) + (1,1) -> (r-1, c-1) + (r-1, c)
        # 0 0 0 0

        # dp bottom up
        dp = [[0.0] * (r+1) for r in range(query_row+2)]
        dp[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                overflow = max(0.0, dp[r][c] - 1.0) / 2.0
                if overflow > 0:
                    dp[r+1][c] += overflow
                    dp[r+1][c+1] += overflow
        
        return min(1.0, dp[query_row][query_glass])



        # dp top down
        def dp(r, c):
            if c < 0 or c > r:
                return 0.0
            
            if r == 0 and c == 0:
                return poured
            
            if (r, c) not in memo:
                left = dp(r-1, c-1)
                right = dp(r-1, c)
                overflow = max(0, left - 1) / 2 + max(0, right - 1) / 2
                memo[(r, c)] = overflow
            
            return memo[(r,c)]

        memo = {}
        return min(1.0, dp(query_row, query_glass))





        # 4 poured
        # 1   => 4 -> 3
        # 1 1 => 3 -> 1
        # 0.25 0.5 0.25 

        glasses = []

        i = 1
        while poured - i >= 0:
            curr = [1] * i
            glasses.append(curr)

            poured -= i
            i += 1
        
        # how many poured left and where is the row now?
        # i = 3
        if poured > 0:
            # i is the how many glass
            # side glass is 1
            # middle glass is 2
            # middle_glass = i - 2 if i > 2 else 0
            # one_portion = float(poured / (i + middle_glass))
            # glasses[i-1][0], glasses[i-1][i-1] = one_portion, one_portion
            # for k in range(1, i-1):
            #     glasses[i-1][k] = one_portion * 2

            rest = [0.0] * i
            middle_glass = i - 2 if i > 2 else 0
            one_portion = poured / (i+middle_glass)
            rest[0], rest[-1] = one_portion, one_portion
            for k in range(1, len(rest)-1):
                res[k] = one_portion * 2
            glasses.append(rest)
        
        if query_row >= len(glasses) or query_glass >= len(glasses):
            return 0.0

        return glasses[query_row][query_glass]