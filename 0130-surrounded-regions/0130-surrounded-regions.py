class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        DIRS = [(-1,0), (1,0), (0,1), (0,-1)]

        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            board[row][col] = 'E'
            for dy, dx in DIRS:
                next_r, next_c = dy+row, dx+col
                if is_within_bounds(next_r, next_c) and board[next_r][next_c] == 'O':
                    dfs(next_r, next_c)

        # first row, last row check for O by column
        for c in range(n):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[m-1][c] == 'O':
                dfs(m-1, c)
        
        # first col, last col check for O by row
        for r in range(m):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][n-1] == 'O':
                dfs(r, n-1)
        print(board)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'