class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # maximum subarray
        # state
        # len i and j

        # bottom up
        m,n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            dp[i][0] = int(nums2[0] == nums1[i])
            res = max(res, dp[i][0])
        for j in range(n):
            dp[0][j] = int(nums1[0] == nums2[j])
            res = max(res, dp[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res
            





        # top down MLE
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            if (i, j) not in memo:
                max_length = 0
                if nums1[i] == nums2[j]:
                    max_length = 1 + dp(i+1, j+1)
                else:
                    max_length = 0
                memo[(i,j)] = max_length

            return memo[(i, j)]
        
        memo = {}
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res = max(res, dp(i,j))
        return res
