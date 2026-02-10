# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # staircase search
        # starting from top-right
        # if curr cell is 1 col - 1
        # if not row + 1

        rows, cols = binaryMatrix.dimensions()
        
        curr_row = 0
        curr_col = cols-1

        while curr_row < rows and curr_col >= 0:
            if binaryMatrix.get(curr_row, curr_col) == 1:
                curr_col -= 1
            else:
                curr_row += 1
        
        return curr_col + 1 if curr_col != cols - 1 else -1



        """
        sorted rows 0, 1
        return the left most having 1 in the column
        
        
        
        
        every row checking
        binary search for 1 lower bound
        
        default float('inf')
        return -1 if answer == float('inf') else answer
        
        time complexity = o(n log n)
        
        
        0 0 0 1 1 
              L       
              R
              M 
        
        """
        
        def lower_bound_binary_search(row, col): # 0, 2
            
            left = 0 # 0
            right = col # 2
            
            while left < right: # 0 < 2
                mid = (left + right) // 2  # mid = 1
                if binaryMatrix.get(row, mid) == 1: # 
                    right = mid
                else:
                    left = mid + 1
            return left
                
        
        rows, cols = binaryMatrix.dimensions()
        leftmost = float('inf')
        for row in range(rows):
            curr = lower_bound_binary_search(row, cols) # 0, 2
            if curr < cols:
                leftmost = min(leftmost, curr)
            
        return leftmost if leftmost != float('inf') else -1