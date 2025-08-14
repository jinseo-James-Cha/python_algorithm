class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            # 한 글자 해석
            res = dfs(i + 1)

            # 두 글자 해석 가능하면 더하기
            if i + 1 < len(s) and int(s[i]) * 10 + int(s[i+1]) <= 26:
                res += dfs(i + 2)                    
            
            memo[i] = res
            return memo[i]
        
        memo = {}
        return dfs(0)