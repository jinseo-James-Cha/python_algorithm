from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Backtracking
        def backtrack(i):
            if i == len(blanks):
                return True
            
            row, col = blanks[i]
            for candi in map(str, range(1, 10)):
                if candi not in rows[row] and candi not in cols[col] and candi not in subBoxes[row//3][col//3]:
                    rows[row].add(candi)
                    cols[col].add(candi)
                    subBoxes[row//3][col//3].add(candi)
                    board[row][col] = candi
                    
                    if backtrack(i+1):
                        return True
                    
                    rows[row].remove(candi)
                    cols[col].remove(candi)
                    subBoxes[row//3][col//3].remove(candi)
                    board[row][col] = "."
            return False
        
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoxes = [[set() for _ in range(3)] for _ in range(3)]
        blanks = []
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    blanks.append((r,c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    subBoxes[r//3][c//3].add(val)
        
        backtrack(0)
        
        
        
        
        

        
    
