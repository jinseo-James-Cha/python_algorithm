from collections import defaultdict
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # start, end 
        # x shot burst -> xstart <= x <= xend
        
        points.sort(key=lambda x : x[1])
        print(points)
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        return arrows