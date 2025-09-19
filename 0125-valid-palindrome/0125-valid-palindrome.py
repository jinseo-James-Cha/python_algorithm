# retry with two pointers inward traversal strategy
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # skip non alphanumeric letter from both pointers
            while left < right and not s[left].isalnum():
            # if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


# New Solution with two pointer
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_s = ""
#         for a in s:
#             if (a >= "a" and a <= "z") or (a >= "A" and a <= "Z") or (a >= "0" and a <= "9"):
#                 new_s += a.lower()

#             # if not a.isalnum(): above or this
#                 # continue
#         # two pointer
#         left = 0
#         for right in range(len(new_s)-1, -1, -1):
#             if left > right:
#                 break
#             if new_s[left] != new_s[right]:
#                 return False
#             left += 1
#         return True


# converting upper into lowercase
# removing all non-alpha

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_s = ""
#         for letter in s:
#             if letter >= "a" and letter <= "z":
#                 new_s += letter
#             elif letter >= "A" and letter <= "Z":
#                 new_s += letter.lower()
#             elif letter >= "0" and letter <= "9":
#                 new_s += letter
            
#         r_new_s = new_s[::-1]

#         if r_new_s == new_s:
#             return True
        
#         return False
        