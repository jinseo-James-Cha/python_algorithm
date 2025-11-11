class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_set = set(word)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(word_index, row, col, visited):
            if board[row][col] != word[word_index]:
                return False
            
            if word_index == len(word)-1:
                return True
            
            visited.add((row,col))
            for dy, dx in DIRS:
                next_r, next_c = dy+row, dx+col
                if is_within_bounds(next_r, next_c) and (next_r, next_c) not in visited:
                    if dfs(word_index+1, next_r, next_c, visited):
                        return True
            visited.remove((row, col))
            return False


        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(0, row, col, set()):
                        return True
        return False