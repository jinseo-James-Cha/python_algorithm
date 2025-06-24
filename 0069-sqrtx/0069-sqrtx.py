class Solution:
    def mySqrt(self, x: int) -> int:
        # spare root x -> ?
        # or nearest integer round down -> 2.82.. -> 2 = int(...)
        # 0 -> 0 #1
        # 1 -> 1, 2, 3  #3
        # 2 -> 4, 5, 6, 7, 8 #5
        # 3 -> 9, 10, 11, 12, 13, 14, 15 # 7
        # 4 -> 16, 17, 18, 19, 20, 21, 22, 23, 24 #9

        # a**2 <= x < a+1**2 ->a
        a = 0
        while a**2 <= 2**31 - 1 :
            if a**2 <= x < (a+1)**2:
                return a
            a += 1
        return 0

        
        