class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_idx = 0
        for t_ch in t:
            if s[s_idx] == t_ch:
                s_idx += 1
            
            if s_idx == len(s):
                return True
        
        return False













        source_len, target_len = len(s), len(t)

        # the source string is empty
        if source_len == 0:
            return True

        # matrix to store the history of matches/deletions
        dp = [ [0] * (target_len + 1) for _ in range(source_len + 1)]

        # DP compute, we fill the matrix column by column, bottom up
        for col in range(1, target_len + 1):
            for row in range(1, source_len + 1):
                if s[row - 1] == t[col - 1]:
                    # find another match
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # retrieve the maximal result from previous prefixes
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

            # check if we can consume the entire source string,
            #   with the current prefix of the target string.
            if dp[source_len][col] == source_len:
                return True

        return False








        # two pointer?
        # one for s one for t
        # if s[slow] == t[fast]: slow += 1
        # if slow == len(s) - 1 : true or not
        
        # a a 0 0
        # x h 1 1, 1 2 1 3 1 4 1 

        slow = fast = 0
        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        
        return slow == len(s)