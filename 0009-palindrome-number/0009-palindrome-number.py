class Solution:
    def isPalindrome(self, x: int) -> bool:
        # all negative cannot be True
        if x < 0:
            return False
        
        x_str = str(x)
        x_str_rev = x_str[::-1]

        return x_str == x_str_rev


        