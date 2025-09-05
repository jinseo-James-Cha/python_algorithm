from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def backtrack(i):
            if i == len(empties):
                return True

            r, c = empties[i]
            for num in map(str, range(1, 10)): # 1~9 and str mapping
                if num not in rows[r] and num not in cols[c] and num not in subBoxes[r // 3][c // 3]:
                
                    rows[r].add(num)
                    cols[c].add(num)
                    subBoxes[int(r / 3)][int(c / 3)].add(num)
                    board[r][c] = num

                    if backtrack(i+1):
                        return True

                    rows[r].remove(num)
                    cols[c].remove(num)
                    subBoxes[int(r / 3)][int(c / 3)].remove(num)
                    board[r][c] = "."
            
            return False

        rows = defaultdict(set)
        cols = defaultdict(set)
        subBoxes = [[set() for _ in range(3)] for _ in range(3)]
        empties = []
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    subBoxes[row // 3][col // 3].add(board[row][col])
                else:
                    empties.append((row, col))
        
        backtrack(0)

        
    
