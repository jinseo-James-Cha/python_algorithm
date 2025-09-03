class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix[i][j] increasing order
        # matrix[i][0] increasing ordr
        m, n = len(matrix), len(matrix[0])

        # binary search - > sorted ok
        # first binary search for lower bound for matrix[i][0]
        # second find the exact target in matrix[i]
        row_num = -1
        for r in range(m):
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] < target:
                row_num = r
        # if not found, return False
        if row_num < 0:
            return False

        for c in range(n):
            if matrix[row_num][c] == target:
                return True

        return False    
