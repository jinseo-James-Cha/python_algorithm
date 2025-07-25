class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 00 01 02 03
        # 10 11 12 13
        # 20 21 22 23
        
        # 3 * 4

        # 20 -> r-c -> 2
        # 10 21 -> 1
        # 00 11 22 -> 0
        # 01 12 23 -> -1
        # 02 13 -> -2
        # 03 -> -3
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
