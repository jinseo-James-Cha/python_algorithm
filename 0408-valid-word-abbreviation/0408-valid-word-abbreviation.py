class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # two pointers on each word and abbr
        left = right = 0
        while left < len(word) and right < len(abbr):
            # validate if the both letters are alphabet
            if abbr[right].isalpha():
                if word[left] == abbr[right]:
                    # alpha and they are matched
                    left += 1
                    right += 1
                    continue
                else:
                    # alpha, but not the same?
                    return False
            
            # abbr has number
            # 1. return False for leading 0
            if  abbr[right] == "0":
                return False
            
            # 2. we should check the following is also num
            # add in temp
            int_right_num = 0
            while right < len(abbr) and not abbr[right].isalpha():
                int_right_num *= 10
                int_right_num += int(abbr[right])
                right += 1
            
            # return False if the num is greater than word length
            if left + int_right_num > len(word):
                return False

            left += int_right_num

        if left == len(word) and right == len(abbr):
            return True
        return False




# with this logic, keep getting wrong answer on different cases..
# I think it is not a good anwer.
# let me think in a different way
# class Solution:
#     def validWordAbbreviation(self, word: str, abbr: str) -> bool:
#         # in abbr -> word? or word -> abbr
#         # 12 is not 1 and 2 
#         # use isalpha() ?

#         # if len is not matching, it must false

#         # I feel like I can using two pointers
#         cur_len = 0
#         translated_abbr = ""

#         left = right = 0
#         while left < len(word):
#             abbr_num = ""
#             while right < len(abbr) and not abbr[right].isalpha():
#                 # return False for leading zero
#                 if not abbr_num and abbr[right] == "0":
#                     return False
#                 abbr_num += abbr[right]
#                 right += 1
            
#             if abbr_num:
#                 left += int(abbr_num)

#                 if left > len(word):
#                     return False

#                 continue

#             if word[left] != abbr[right]:
#                 return False

#             left += 1
#             right += 1

#         return True if len(word) -1 == left and len(abbr) -1 == right else False
            
