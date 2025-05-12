class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
         # 3x3 박스 체크용 3차원 배열 (3x3x10)
        box_check = [[[False] * 10 for _ in range(3)] for _ in range(3)]

        for r in range(9):
            row_check = [False] * 10
            col_check = [False] * 10

            for c in range(9):
                # -----------------------------
                # 행 검사
                if board[r][c] != ".":
                    num = int(board[r][c])
                    if row_check[num]:
                        return False
                    row_check[num] = True

                    # 3x3 박스 검사
                    box_r, box_c = r // 3, c // 3
                    if box_check[box_r][box_c][num]:
                        return False
                    box_check[box_r][box_c][num] = True

                # -----------------------------
                # 열 검사
                if board[c][r] != ".":
                    num = int(board[c][r])
                    if col_check[num]:
                        return False
                    col_check[num] = True

        return True