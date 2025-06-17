# this is answer and I think it looks better
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         # two pointer 
#         left = 0
#         right = len(s) - 1
#         left_deleted = False
#         right_deleted = False
#         retry_index = []
#         while left < right:
#             if s[left] != s[right]:
#                 if left_deleted and right_deleted:
#                     return False
#                 else:
#                     if not left_deleted:
#                         left_deleted = True
#                         retry_index = [left, right]
#                         left += 1
#                     elif not right_deleted:
#                         right_deleted = True
#                         left, right = retry_index
#                         right -= 1
#                     continue
#             left += 1
#             right -= 1
#         return True