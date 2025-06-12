# v2: optimize
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:   
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        subBoxes = [[set() for _ in range(3)] for _ in range(3)] # subBoxes[][] = set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in rows[r]:
                    return False
                if num in columns[c]:
                    return False
                if num in subBoxes[r // 3][c // 3]:
                    return False
                
                rows[r].add(num)
                columns[c].add(num)
                subBoxes[r // 3][c // 3].add(num)
        return True

# [".",".","4"   ,".",".","."   ,"6","3","."],
# [".",".","."   ,".",".","."   ,".",".","."]
# ["5",".","."   ,".",".","."   ,".","9","."]

# [".",".","."   ,"5","6","."   ,".",".","."]
# ["4",".","3"   ,".",".","."   ,".",".","1"]
# [".",".","."   ,"7",".","."   ,".",".","."]


# [".",".","."   ,"5",".","."   ,".",".","."]
# [".",".","."   ,".",".","."   ,".",".","."]
# [".",".","."   ,".",".","."   ,".",".","."]]

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:        
#         # should I break down by row, column and 3x3?
#         sub_boxes = [[set() for _ in range(3)] for _ in range(3)]
#         for r in range(9):
#             row = set()
#             column = set()
#             for c in range(9):
#                 # row check
#                 r_num = board[r][c]
#                 if r_num != ".":
#                     if r_num in row:
#                         return False
#                     else:
#                         row.add(r_num)
#                 # column check
#                 c_num = board[c][r]
#                 if c_num != ".":
#                     if c_num in column:
#                         return False
#                     else:
#                         column.add(c_num)

#                 # how can I check sub box
#                 # which data structure?
#                 # there are 9 subboxes
#                 # [r // 3][c // 3] -> one box!
#                 if r_num != ".":
#                     if r_num in sub_boxes[r // 3][c // 3]:
#                         return False
#                     else:
#                         sub_boxes[r // 3][c // 3].add(r_num)
#                 # if c_num != "." and r != c:
#                 #     if c_num in sub_boxes[c // 3][r // 3]:
#                 #         return False
#                 #     else:
#                 #         sub_boxes[c // 3][r // 3].add(c_num)
#             # print(c)
#             # print(r)
#         return True











# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:        
#          # 3x3x10 -> 10False in a box and 3 * 3 box
#         box_check = [[[False] * 10 for _ in range(3)] for _ in range(3)]

#         for r in range(9):
#             row_check = [False] * 10
#             col_check = [False] * 10

#             for c in range(9):
#                 # -----------------------------
#                 # row
#                 if board[r][c] != ".":
#                     num = int(board[r][c])
#                     if row_check[num]:
#                         return False
#                     row_check[num] = True

#                     # 3x3 box
#                     box_r, box_c = r // 3, c // 3
#                     if box_check[box_r][box_c][num]:
#                         return False
#                     box_check[box_r][box_c][num] = True

#                 # col
#                 if board[c][r] != ".":
#                     num = int(board[c][r])
#                     if col_check[num]:
#                         return False
#                     col_check[num] = True

#         return True