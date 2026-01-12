class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # n = len(points)
        # points[i] = [xi, yi]
        # return minimum time in seconds to visit all points..
        # minimum_time += max(abs(x1-x2), (y1-y2))

        n = len(points)
        minimum_time = 0
        for i in range(n-1):
            minimum_time += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1]-points[i+1][1]))
        return minimum_time