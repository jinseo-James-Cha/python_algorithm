class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # 1. find a maximum value in col
        # 2. 

        m, n = len(mat), len(mat[0])
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2

            # 1.
            max_row = 0
            for r in range(m):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r
            
            # 2.
            val = mat[max_row][mid]
            left_val = mat[max_row][mid-1] if mid > 0 else -1
            right_val = mat[max_row][mid+1] if mid < n-1 else -1

            # find the peack
            if left_val < val > right_val:
                return [max_row, mid]
            elif left_val > val:
                right = mid-1
            else:
                left = mid + 1
        
        return [-1, -1]




        # Strictly greater than 4directions
        # find a peak in every row and check row-1 and row +1 values
        def check_other_rows(row, col, peak_val):
            if row < 0 or row >= len(mat):
                return True
            
            return mat[row][col] < peak_val

        def get_peak_col(row):
            left = 0
            right = len(row) - 1
            while left < right:
                mid = (left + right) // 2
                if row[mid] < row[mid+1]:
                    left = mid+1
                else:
                    right = mid
            return left
        
        for i, curr_row in enumerate(mat):
            peak_col = get_peak_col(curr_row)
            up_score = check_other_rows(i-1, peak_col, mat[i][peak_col])
            down_score = check_other_rows(i+1, peak_col, mat[i][peak_col])
            if up_score and down_score:
                return [i, peak_col]
        
        return [-1,-1]

        





        # dfs 
        # time = O of m times n
        m, n = len(mat), len(mat[0])

        def is_within_bound(row,col):
            if row < 0 or row >= len(mat):
                return False
            
            if col < 0 or col >= len(mat[0]):
                return False
            
            return True

        def dfs(row, col, val):
            if not is_within_bound(row, col):
                return 1
            
            return int(mat[row][col] < val)


        for row in range(m):
            for col in range(n):
                up = dfs(row-1, col, mat[row][col])
                down = dfs(row+1, col, mat[row][col])
                left = dfs(row, col-1, mat[row][col])
                right = dfs(row, col+1, mat[row][col])
                if up+down+left+right == 4:
                    return [row, col]

        return [-1, -1]