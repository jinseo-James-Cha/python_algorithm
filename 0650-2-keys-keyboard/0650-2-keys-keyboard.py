class Solution:
    def minSteps(self, n: int) -> int:
        # one of two operations
        # 1. copy all - copy the whole characters
        # 2. paste - paste copied characters


        # n -> return the minimum number of operations to get the character 'A' exactly n times

        # starting with 'A'
        # n
        # 1 2               3                   4                   5
        # 0 copy and past  copy and past past  copy past copy past  copy paste paste paste paste


        """
        n
        1 A  X 
        3 AAA copy paste2 paste*1
        5 AAAAA copy past2 past*3 -> dp[5] = dp[2] + 3
        7 AAAAAAA copy past past*5

        2 AA copy paste -> dp[2] = 2
        4 AAAA copy paste copy past -> dp[4] = dp[2] + 2 = 4
        6 AAAAAA copy past copy past past -> dp[6] = dp[4] + 1 = 5
        8 AAAAAAAA copy past copy past copy past -> dp[8] = dp[6] + 1
        10 AAAAAAAAAA copy past copy past past past past = dp[8] = dp[6] + 2
        """
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = i 
            
            for j in range(1, (i // 2) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
                    
        return dp[n]