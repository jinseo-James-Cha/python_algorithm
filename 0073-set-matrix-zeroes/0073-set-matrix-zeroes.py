class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first I need r,c for all 0?
        rows = set()
        cols = set()
        
        m = len(matrix) # r
        n = len(matrix[0]) # c
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for row in rows:
            matrix[row] = [0] * n
        
        for col in cols:
            for i in range(m): 
                matrix[i][col] = 0


        
        