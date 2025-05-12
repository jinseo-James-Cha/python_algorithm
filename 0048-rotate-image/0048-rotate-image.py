class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        test = [[0] * len(matrix) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                test[j][-i-1] = matrix[i][j]
        matrix[:] = test       