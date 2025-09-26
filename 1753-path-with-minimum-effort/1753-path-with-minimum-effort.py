from collections import defaultdict
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # dijkstra
        # heapq, while, relax
        def is_within_bound(x, y):
            return 0 <= x < len(heights) and 0 <= y < len(heights[0])

        row, col = len(heights), len(heights[0])
        dist_matrix = [[float(inf)] * col for _ in range(row)]
        dist_matrix[0][0] = 0
        
        visited = [[False] * col for _ in range(row)]
        pq = [(0, 0, 0)] # diff, x, y

        DIR = [(-1,0), (1,0), (0,-1), (0,1)]
        while pq:
            diff, x, y = heapq.heappop(pq)
            visited[x][y] = True
            for dx, dy in DIR:
                next_x, next_y = x+dx, y+dy
                if is_within_bound(next_x, next_y) and not visited[next_x][next_y]:
                    curr_diff = abs(heights[next_x][next_y] - heights[x][y])
                    max_diff = max(curr_diff, dist_matrix[x][y])
                    
                    if dist_matrix[next_x][next_y] > max_diff:
                        dist_matrix[next_x][next_y] = max_diff
                        heapq.heappush(pq, (max_diff, next_x, next_y))
        return dist_matrix[-1][-1]