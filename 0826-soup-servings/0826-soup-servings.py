class Solution:
    def soupServings(self, n: int) -> float:
        # two soups A B
        # starting n
        # one of these four by RANDOM -> 0.25 % each
        # 1. A + 100 / B + 0
        # 2. A 75 / B + 25
        # 3. A 50 / B + 50
        # 4. A 25 / B + 75

        # n 50
        # A 50 / B 50
        # 1. 150 / 50
        # 2. 125 / 75
        # 3. 100 / 100
        # 4. 75 / 125
        # top down
        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            
            return 0.25 * (dp(a-4,b) + dp(a-3, b-1) + dp(a-2, b-2) + dp(a-1, b-3))

        m = ceil(n / 25) 
        for k in range(1, m + 1):
            if dp(k, k) > 1 - 10**-5:
                return 1.0
        return dp(m, m)