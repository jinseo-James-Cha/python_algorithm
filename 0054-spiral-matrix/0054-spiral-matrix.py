class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        top = left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        res = []
        while top <= bottom and left <= right: 
            # move right
            for r in range(left, right + 1):
                res.append(matrix[top][r])
            top += 1

            # move down
            for b in range(top, bottom + 1):
                res.append(matrix[b][right])
            right -= 1
            
            # move left
            if top <= bottom:
                for l in range(right, left - 1 , -1):
                    res.append(matrix[bottom][l])
                bottom -= 1

            # move up
            if left <= right:
                for u in range(bottom, top - 1, -1):
                    res.append(matrix[u][left])
                left += 1
        return res
        
