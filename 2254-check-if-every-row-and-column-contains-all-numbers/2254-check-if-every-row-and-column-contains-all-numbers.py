class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row, col in zip(matrix, zip(*matrix)):
            if len(set(row)) != n or len(set(col)) != n:
                return False
        return True


        # n * n
        # is it \ the same / all different?
        # brute force O(n^2)
        # n = len(matrix)
        # for r in range(n):
        #     r_set = set()
        #     c_set = set()
        #     for c in range(n):
        #         r_set.add(matrix[r][c])
        #         c_set.add(matrix[c][r])
        #     if len(r_set) != n or len(c_set) != n:
        #         return False
        # return True
            