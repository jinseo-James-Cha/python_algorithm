class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        """
        m, n grid -> 0, 1, 2
        start 0,0
        end m-1, n-1

        direction right down

        0 -> 0 score and 0 cost
        1 -> 1 score and 1 cost
        2 -> 2 score and 1 cost

        return maximum score without exceeding total cost k
        if not, -1
        """
        # DP - bottom up
        m, n = len(grid), len(grid[0])

        INF = float("-inf")
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == INF:
                        continue

                    if i + 1 < m:
                        val = grid[i + 1][j]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i + 1][j][c + cost] = max(
                                dp[i + 1][j][c + cost], dp[i][j][c] + val
                            )

                    if j + 1 < n:
                        val = grid[i][j + 1]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i][j + 1][c + cost] = max(
                                dp[i][j + 1][c + cost], dp[i][j][c] + val
                            )

        ans = max(dp[m - 1][n - 1])
        return -1 if ans < 0 else ans


        # DP - top down -> memory limit exceeded -> O(M*N*K)
        m, n = len(grid), len(grid[0])
        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def dp(row, col, remaining):
            if remaining < 0:
                return float('-inf')
            
            if row == m-1 and col == n-1:
                return grid[row][col]
            
            if (row, col, remaining) not in memo:
                res = float('-inf')
                curr = grid[row][col]
                for dr, dc in [(0,1), (1,0)]:
                    next_r, next_c = row+dr, col+dc
                    if is_within_bounds(next_r, next_c):
                        cost = 1 if grid[next_r][next_c] != 0 else 0
                        if remaining >= cost:
                            sub_res = dp(next_r, next_c, remaining - cost)
                            if sub_res != float('-inf'):
                                res = max(res, curr + sub_res)

                memo[(row, col, remaining)] = res
            
            return memo[(row, col, remaining)]

        memo = {}
        start_cost = 1 if grid[0][0] != 0 else 0
        if start_cost > k:
            return -1
            
        ans = dp(0, 0, k - start_cost)
        return -1 if ans == float("-inf") else ans