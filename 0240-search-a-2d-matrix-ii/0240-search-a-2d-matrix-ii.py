class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height, width = len(matrix), len(matrix[0])

        row = height - 1
        col = 0
        
        # target보다 클때는 row를 줄이고
        # target보다 작을때는 col을 줄이는 전략이라서
        # 왼쪽 맨 밑에서 시작하는구나.
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False


        # divide and conquer
        if not matrix:
            return False
        
        def search_rec(left, up, right, down):
            if left > right or up > down:
                return False
            
            if target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = (left + right) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)
        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)