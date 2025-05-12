class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True


        # This is My solution which is not completed :(
        # for r in range(9):
        #     row_check = [False] * 10
        #     col_check = [False] * 10
        #     box_check = [[False] * 3 ]            
            
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue

        #         # row
        #         if row_check[int(board[r][c])]:
        #             return False
        #         else:
        #             row_check[int(board[r][c])] = True
                
        #         # col
        #         if col_check[int(board[c][r])]:
        #             return False
        #         else:
        #             col_check[int(board[c][r])] = True
                
                # sub-box
                # if board[i % 3][j % 3] != ".":
        
        # # sub-box check
        # for i in range(9):
        #     check = [False] * 10
        #     for j in range(9):
        #         if board[i % 3][j % 3] != ".":
        #             if check[int(board[i % 3])][int(board[j % 3])]:
        #                     return False
        #             else:
        #                 check[int(board[i % 3])][int(board[j % 3])] = True

        # return True
        
        