class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                return 1
            res = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals or col in cols:
                    continue
                
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                cols.add(col)

                res += backtrack(row + 1, diagonals, anti_diagonals, cols)

                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                cols.remove(col)
            return res

        return backtrack(0, set(), set(), set())