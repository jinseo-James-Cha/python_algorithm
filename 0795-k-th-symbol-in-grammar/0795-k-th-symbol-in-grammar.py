from collections import deque
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # n 1 ~
        # 0 -> 01
        # 1 -> 10

        # n = 3
        # 1st 0 -> 2**0
        # 2nd 01 -> 2**1
        # 3rd 0110 -> 2**2
        # 4th 01101001 -> 2**3
        # 5th 0110100110010110
        
        # recursive 
        if n == 1:
            return 0

        parent = self.kthGrammar(n-1, math.ceil(k/2))
        is_odd = k % 2 == 1

        if parent == 0:
            return 0 if is_odd else 1
        else:
            return 1 if is_odd else 0
        
        # bfs -> MLE
        i = 1
        res = [["0"]]
        while i < n:
            last = res[-1]
            curr = ""
            for l in last:
                if l == "0":
                    curr += "01"
                else:
                    curr += "10"
            
            res.append(list(curr))
            i += 1
        return int(res[-1][k-1])
