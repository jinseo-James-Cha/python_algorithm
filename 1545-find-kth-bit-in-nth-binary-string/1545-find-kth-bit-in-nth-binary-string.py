class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # using the formular -> dp?
        def invert_and_reverse(s):
            res = []
            for ch in s: # 1 1 0 -> 0 0 1
                if ch == "0":
                    res.append("1")
                else:
                    res.append("0")
            res.reverse()
            return "".join(res)


        def dp(i):
            if i == 1:
                return "0"
            
            if i not in memo:
                prev = dp(i-1)
                in_re_prev = invert_and_reverse(prev)
                memo[i] = prev + "1" + in_re_prev

            return memo[i]
        
        memo = {}
        res = dp(n)
        return res[k-1] 