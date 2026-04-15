class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        brute force 
        check every each cell and compare values on 4 directions cells within the bounds.

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