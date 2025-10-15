class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        top, right, bottom, left = 0, len(matrix[0])-1, len(matrix)-1, 0 

        res = []
        while top <= bottom and left <= right:
            # to right
            for next_right in range(left, right+1): 
                res.append(matrix[top][next_right])
            top += 1 
            
            # to bottom
            for next_bottom in range(top, bottom+1):
                res.append(matrix[next_bottom][right])
            right -= 1
            
            # to left
            if top <= bottom:
                for next_left in range(right, left-1, -1):
                    res.append(matrix[bottom][next_left])
                bottom -= 1
            
            # to top
            if left <= right:
                for next_top in range(bottom, top-1, -1):
                    res.append(matrix[next_top][left])
                left += 1
        return res












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
        
