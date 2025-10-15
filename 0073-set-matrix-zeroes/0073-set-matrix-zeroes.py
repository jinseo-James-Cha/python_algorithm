# optimize to make 
# time : N + M +  M*N -> O(M*N)
# space : O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        # rows
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        







        # using markers into first row and column
        # check there is already first row and column has zero

        # m, n = len(matrix), len(matrix[0])

        # # check first row has zero
        # first_row_has_zero = False
        # for c in range(n):
        #     if matrix[0][c] == 0:
        #         first_row_has_zero = True
        #         break
        
        # # check first col has zero
        # first_col_has_zero = False
        # for r in range(m):
        #     if matrix[r][0] == 0:
        #         first_col_has_zero = True
        #         break
        
        # # mark first row or col if there is 0 in it
        # for r in range(1, m):
        #     for c in range(1, n):
        #         if matrix[r][c] == 0:
        #             matrix[0][c] = 0
        #             matrix[r][0] = 0

        # # update other row and col if there is marker
        # for r in range(1, m):
        #     for c in range(1, n):
        #         if matrix[0][c] == 0 or matrix[r][0] == 0:
        #             matrix[r][c] = 0

        # # if first row has zero already without marker, update too
        # if first_row_has_zero:
        #     for c in range(n):
        #         matrix[0][c] = 0

        # # col too
        # if first_col_has_zero:
        #     for r in range(m):
        #         matrix[r][0] = 0



# time O(M * N)
# space O(M + N)
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # first I need r,c for all 0?
#         rows = set()
#         cols = set()
        
#         m = len(matrix) # r
#         n = len(matrix[0]) # c
#         for r in range(m):
#             for c in range(n):
#                 if matrix[r][c] == 0:
#                     rows.add(r)
#                     cols.add(c)
        
#         # reset whole rows into 0
#         for row in rows:
#             matrix[row] = [0] * n
        
#         # reset one by one in cols
#         for col in cols:
#             for i in range(m): 
#                 matrix[i][col] = 0