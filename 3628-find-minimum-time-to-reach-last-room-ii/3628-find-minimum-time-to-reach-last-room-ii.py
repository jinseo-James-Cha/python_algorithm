class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # start 0,0 and 0 
        # move adjacent

        # +1 +2 +1 +2 +1 +2.....

        # dijkstra
        n, m = len(moveTime), len(moveTime[0])
        inf = float('inf')
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]

        dirs = [(1,0), (-1,0), (0, 1), (0,-1)]
        d[0][0] = 0
        pq = []
        heapq.heappush(pq, (0,0,0))
        while pq:
            curr_dis, r, c = heapq.heappop(pq)
            if v[r][c]:
                continue
            
            if r == n-1 and c == m-1:
                break
            
            v[r][c] = 1
            for dx, dy in dirs:
                next_x, next_y = dx + r, dy + c
                if not (0 <= next_x < n and 0 <= next_y < m):
                    continue
                dist = max(d[r][c], moveTime[next_x][next_y]) + (r + c) % 2 + 1
                if d[next_x][next_y] > dist:
                    d[next_x][next_y] = dist
                    heapq.heappush(pq, (dist, next_x, next_y))
        return d[n-1][m-1]