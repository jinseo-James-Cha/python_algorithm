import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # get minimum among a maximum in a path

        # dijkstra
        def is_within_bound(r, c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])

        rows, cols = len(heights), len(heights[0])
        diff_matrix = [[float('inf')] * cols for _ in range(rows)]
        diff_matrix[0][0] = 0
        visited = [[False] * cols for _ in range(rows)]

        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        pq = [(0,0,0)]
        while pq:
            max_diff, r, c = heapq.heappop(pq)
            visited[r][c] = True
            if r+1 == rows and c+1 == cols:
                return max_diff
            
            for dy, dx in DIR:
                next_x, next_y = r+dy, c+dx
                if is_within_bound(next_x, next_y) and not visited[next_x][next_y]:
                    curr_diff = abs(heights[r][c] - heights[next_x][next_y])
                    new_diff = max(curr_diff, diff_matrix[r][c])
                    
                    if diff_matrix[next_x][next_y] > new_diff:
                        diff_matrix[next_x][next_y] = new_diff
                        heapq.heappush(pq, (new_diff, next_x, next_y))
        return diff_matrix[-1][-1]