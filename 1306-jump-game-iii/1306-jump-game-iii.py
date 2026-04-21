class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        - arr[i] > 0

        - starting from start index

        - i + arr[i] or i - arr[i]

        - return any index has 0

        """
        #  DP
        # state i
        # - is i in range of the array? 
        # - is i == 0? 
        # - or move other index
        
        n = len(arr)
        if start >= n:
            return False

        if arr[start] == 0:
            return True

        def dp(i):
            if i < 0 or i >= len(arr):
                return False
            
            if i in visited:
                return False
            
            visited.add(i)

            if i not in memo:
                if arr[i] == 0:
                    memo[i] = True
                else:
                    memo[i] = dp(i + arr[i]) or dp(i - arr[i])
            return memo[i]
        
        memo = {}
        visited = set()
        return dp(start)
    