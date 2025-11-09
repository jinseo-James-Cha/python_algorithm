import heapq
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # shortest path - bfs - dijkstra algorithm
        # but this weight is the same with 1, so can be optimized with BFS.
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(n))
        for row in range(n-1, -1, -1):
            for col in columns:
                cells[label] = (row, col)
                label += 1
            columns.reverse()
        
        # dijkstra algorithm
        dist = [-1] * (n**2 + 1)
        dist[1] = 0
        q = [(0, 1)]
        while q:
            d, curr = heapq.heappop(q) # reach curr by d times
            if dist[curr] != d:
                continue

            for nxt in range(curr+1, min(curr+6, n**2) + 1):
                row, col = cells[nxt]
                destination = board[row][col] if board[row][col] != -1 else nxt
                if dist[destination] == -1 or dist[destination] > dist[curr] + 1:
                    dist[destination] = dist[curr] + 1
                    heapq.heappush(q, (dist[destination], destination))
        return dist[n**2]
            

