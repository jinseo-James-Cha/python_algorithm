# this is the kick....
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True

# let me do another idea
# v3 : fill up with 0 and then compare them
# class Solution:
#     def validWordSquare(self, words: List[str]) -> bool:
#         # standarize with row len
#         row_len = len(words)
#         col_len = len(words[0])
#         for w in words:
#             col_len = max(col_len, len(w))
#         max_len = max(row_len, col_len)

#         # make same rows if col is greater than row
#         for i in range(max_len - row_len):
#             words.append("0" * col_len)
#         row_len = max_len

#         # make same cols if row is greater than col
#         for i in range(row_len):
#             if len(words[i]) != row_len:
#                 words[i] += "0" * (row_len - len(words[i]))

#         for r in range(row_len):
#             for c in range(row_len):
#                 if words[r][c] != words[c][r]:
#                     return False
#         return True

# 1 <= words.length <= 500
# 1 <= words[i].length <= 500

# v2: let me compare one by one 
# a,n,m,e is the same letter for row and column
# 00 11 22 33 skip
# 
# class Solution:
#     def validWordSquare(self, words: List[str]) -> bool:
#         for r in range(len(words)):
#             print(len(words[r]))
#             for c in range(len(words[r])):
#                 break
#                 if r == c:
#                     print(r,c)
#                 # print(r,c)
#                 # if words[r][c]:
#                 #     print(words[r][c])
#                 # if words[c][r]:
#                 #     print(words[c][r])
#                 #     # return False
#         return True




# I think its can be O(N^2) !
# I can have rows to be compared, so I need colums!


# 0 <= k < max(numRows, numColumns) this is the key
# class Solution:
#     def validWordSquare(self, words: List[str]) -> bool:
#         columns = []
#         for i in range(len(words[0])):
#             j = 0
#             temp_col = ""
#             while j < len(words[i]):
#                 # if not words[j][i]: is out of range
#                 # need to check by len
#                     # return False
#                 temp_col += words[j][i]
#                 j += 1
#             columns.append(temp_col)
#             print(columns)
        
#         # compare rows and colums
#         for i in range(len(words)):
#             if words[i] != columns[i]:
#                 return False
#         return True