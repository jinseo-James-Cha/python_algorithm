# converting upper into lowercase
# removing all non-alpha

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for letter in s:
            if letter >= "a" and letter <= "z":
                new_s += letter
            elif letter >= "A" and letter <= "Z":
                new_s += letter.lower()
            elif letter >= "0" and letter <= "9":
                new_s += letter
            
        r_new_s = new_s[::-1]

        if r_new_s == new_s:
            return True
        
        return False
        