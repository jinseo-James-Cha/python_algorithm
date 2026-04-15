class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        binary search
        search a column with binary search that is greater than left and right
        if you find a col -> search a row in the column that is greater than up and bottm
        -> return the row, col
        """
        m, n = len(mat), len(mat[0])
        
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            
            # find biggiest one in the row
            max_row = 0
            for r in range(1, m):
                if mat[max_row][mid] < mat[r][mid]:
                    max_row = r

            left_val = mat[max_row][mid-1] if mid > 0 else -1
            right_val = mat[max_row][mid + 1] if mid < n - 1 else -1

            if left_val < mat[max_row][mid] > right_val:
                return [max_row, mid]
            elif left_val > mat[max_row][mid]:
                right = mid - 1
            elif right_val > mat[max_row][mid]:
                left = mid + 1
        return [-1, -1]
            








        """
        brute force 
        check every each cell and compare values on 4 directions cells within the bounds.

        O(n * m * 4) -> O(n * m)
        """
        def is_within_bound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        DIRS = [(0,-1), (0,1), (-1,0), (1,0)]
        def is_peak_element(row, col):
            check_all = 0
            for dr, dc in DIRS:
                next_r, next_c = row + dr, col + dc
                if not is_within_bound(next_r, next_c):
                    check_all += 1 
                elif mat[next_r][next_c] < mat[row][col]:
                    check_all += 1
            return check_all == 4

        count_peak_elements = 0
        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(n):
                if is_peak_element(row, col):
                    return [row,col]
        return []