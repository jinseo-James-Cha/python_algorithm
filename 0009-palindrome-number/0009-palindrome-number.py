# Follow up: Could you solve it without converting the integer to a string?
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # all negative cannot be True
        if x < 0:
            return False

        # copy original
        original = x

        # for loop from the back
        back_num = 0
        while x > 0:
            back_num *= 10
            back_num += x % 10
            x = x // 10
        
        return original == back_num
            


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # all negative cannot be True
#         if x < 0:
#             return False
        
#         x_str = str(x)
#         x_str_rev = x_str[::-1]

#         return x_str == x_str_rev


        