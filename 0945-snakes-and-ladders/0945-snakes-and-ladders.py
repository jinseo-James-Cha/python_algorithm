class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        

        # BFS - dijkstra algorithm - shortest path with weight and directed
        n = len(board)
        cells = [None] * (n*n + 1)
        label = 1
        cols = list(range(n))
        for row in range(n-1, -1, -1):
            for col in cols:
                cells[label] = (row, col)
                label += 1
            cols.reverse()
        
        dist = [-1] * (n*n+1)
        dist[1] = 0
        queue = [(0, 1)]
        while queue:
            curr_d, curr_cell = heapq.heappop(queue)
            if curr_d != dist[curr_cell]:
                continue
            
            for nxt in range(curr_cell+1, min(curr_cell+6, n*n) + 1):
                row, column = cells[nxt]
                destination = (board[row][column] if board[row][column] != -1 else nxt)

                if dist[destination] == -1 or dist[curr_cell] + 1 < dist[destination]:
                    dist[destination] = dist[curr_cell] + 1
                    heapq.heappush(queue, (dist[destination], destination))
        return dist[n*n]