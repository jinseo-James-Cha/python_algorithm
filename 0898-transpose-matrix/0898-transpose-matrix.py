class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # if row == col -> nothing
        # if row != col -> a[i][j] -> a[j][i]
        row = len(matrix)
        col = len(matrix[0])

        res = [[0] * row for _ in range(col)]
        for r in range(row):
            for c in range(col):
                res[c][r] = matrix[r][c]
        
        return res