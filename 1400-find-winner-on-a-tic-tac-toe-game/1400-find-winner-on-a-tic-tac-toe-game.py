class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def rowCheck(row: int, board: List[List[int]]) -> bool:
            a,b,c = board[row]
            if a == b == c:
                return True
            return False

        def colCheck(col: int, board: List[List[int]]) -> bool:
            a,b,c = [board[i][col] for i in range(3)]
            if a == b == c:
                return True
            return False
        
        def diaCheck(board: List[List[int]]) -> bool:
            a1,b1,c1 = [board[i][i] for i in range(3)]
            if a1 != ' ' and a1 == b1 == c1:
                return True
            
            a2,b2,c2 = [board[0][2], board[1][1], board[2][0]]
            if a2 != ' ' and a2 == b2 == c2:
                return True
            return False
        # 3 * 3
        # ' '
        # A -> 'X' , B-> 'O' into ' ' empty paces
        # end 1) 3 the same row, column, diagonal(cross)
        # end 2) there is non empty
        board = [ [' '] * 3 for _ in range(3)]
        count = 0
        turn = True # True -> A and start from A
        for x, y in moves:
            if board[x][y] == ' ':
                if turn:
                    board[x][y] = "X"
                else:
                    board[x][y] = "O"
            if rowCheck(x, board):
                return "A" if turn else "B"
            if colCheck(y, board):
                return "A" if turn else "B"
            if diaCheck(board):
                return "A" if turn else "B"
            turn = not turn
            count += 1
        
        if count != 9:
            return "Pending"
        return "Draw"