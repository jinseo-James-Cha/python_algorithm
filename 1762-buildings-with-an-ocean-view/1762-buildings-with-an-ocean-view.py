class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        questions
        - n buildings -> n = len(heights)
        - ocean is the right side ->

        4 2 3 1
        -
            -
          -
              -
        the rightmost building is always ocean view

        tracking the highest building on rightside and compare with its building
        if curr building is higher than the maximum building on right side, 
        it is the answer.

        <- backward traversal?

        """

        # 4 2 3 1
        
        # res [3]
        # 3 > 1 == res[-1]  O
        # res [3, 2]
        # 2 > 3 == res[2] X
        # res [3, 2]
        # 4 > 3 == res[2] O
        # res [3, 2, 0]

        n = len(heights)
        res = [n-1]
        for i in range(n-2, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)
        
        return res[::-1]
                
