class Solution:
    def isArmstrong(self, n: int) -> bool:
        # 1. problem
        # armstrong -> sum each kth num **3
        # 1 5 3 -> 1**len(str(153)) + 5**3 + 3**3

        # 1. intuition
        # I need I to dynamically assign the len -> 
        # loop cur % 10 and **3 -> res and check res == original n
        
        # 2. complexicy
        # O(n) -> 10^8 -> ok

        # 3. data structure
        # int[] and int res

        res = 0
        cur = n
        k = len(str(n))
        for i in range(k):
            remainder = cur % 10
            res += remainder**k
            cur //= 10
        return res == n