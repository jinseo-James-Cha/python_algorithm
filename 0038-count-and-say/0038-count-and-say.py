class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        curr_count = 1
        curr_ch = prev[0]

        res = ""
        for i in range(1, len(prev)):
            if curr_ch != prev[i]:
                res += str(curr_count) + curr_ch
                curr_count = 1
                curr_ch = prev[i]
            else:
                curr_count += 1
        
        res += str(curr_count) + curr_ch
        return res
                
                