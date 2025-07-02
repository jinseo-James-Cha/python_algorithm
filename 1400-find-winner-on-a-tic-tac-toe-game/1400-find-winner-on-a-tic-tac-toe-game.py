class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def rowCheck(row: int, board: List[List[int]]) -> bool:
            a,b,c = board[row]
            return a != ' ' and a == b == c

        def colCheck(col: int, board: List[List[int]]) -> bool:
            a,b,c = [board[i][col] for i in range(3)]
            return a != ' ' and a == b == c
        
        def diaCheck(board: List[List[int]]) -> bool:
            if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
                return True
            if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
                return True
            return False
        # 3 * 3
        # ' '
        # A -> 'X' , B-> 'O' into ' ' empty paces
        # end 1) 3 the same row, column, diagonal(cross)
        # end 2) there is non empty
        board = [[' '] * 3 for _ in range(3)]
        turn = True  # True: A ("X"), False: B ("O")

        for x, y in moves:
            board[x][y] = "X" if turn else "O"
            if rowCheck(x, board) or colCheck(y, board) or diaCheck(board):
                return "A" if turn else "B"
            turn = not turn
        return "Draw" if len(moves) == 9 else "Pending"