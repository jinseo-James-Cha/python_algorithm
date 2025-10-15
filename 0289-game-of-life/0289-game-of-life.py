class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live 1, dead 0
        # is_live = True
        # 8 neighbors
        # live cell -> dead when 0 or 1 live neighbors
        # live cell -> live when 2 or 3 live neighbors
        # live cell -> dead when more than 3 live neighbors
        # dead cell -> live when 3 == live neighbors 

        m,n = len(board), len(board[0])
        next_gen = [[[0,0] for _ in range(n)] for _ in range(m)]

        def is_within_board(r, c):
            return 0 <= r < m and 0 <= c < n

        DIRS = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
        for i in range(m):
            for j in range(n):
                lives = 0
                deads = 0
                for dy, dx in DIRS:
                    next_r, next_c = i+dy, j+dx
                    if is_within_board(next_r, next_c):
                        if board[next_r][next_c]:
                            lives += 1
                        else:
                            deads += 1
                next_gen[i][j][0] = deads
                next_gen[i][j][1] = lives

        for i in range(m):
            for j in range(n):
                # dead -> 
                if board[i][j] == 0:
                    if next_gen[i][j][1] == 3: # reproduction
                        board[i][j] = 1
                # live ->
                else:
                    if next_gen[i][j][1] < 2: # under-population
                        board[i][j] = 0
                    elif next_gen[i][j][1] > 3: # over-population
                        board[i][j] = 0

