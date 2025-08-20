class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        i = 2
        while i**2 <= num:
            if i**2 == num:
                return True
            i += 1
        return False


        # 1 2 3 4 5
        # 1 4 9 16 25
        # if num == 1:
        #     return True
        # for i in range(1, num):
        #     quotient = num // i
        #     remainder = num % i
        #     if quotient == i and 0 == remainder:
        #         return True
        # return False