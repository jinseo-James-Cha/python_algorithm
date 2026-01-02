from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        from entrance to exit ... nearest.. -> bfs smell
        
        maze[i] = '.' empty or '+' wall

        one step -> up down left right
        no step to wall and out of maze

        exit -> boarder and empty cell
        """
        m, n = len(maze), len(maze[0])
        DIRS = [(-1,0), (1,0), (0,-1), (0,1)]

        queue = deque([(entrance[0], entrance[1], 0)])  # 괄호 하나 더!
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            row, col, step = queue.popleft()

            for dy, dx in DIRS:
                next_row, next_col, next_step = row+dy, col+dx, step+1
                if (0 <= next_row < m and 0 <= next_col < n) and maze[next_row][next_col] == '.':
                    if next_row == 0 or next_row == m-1 or next_col == 0 or next_col == n-1:
                        return next_step

                    maze[next_row][next_col] = '+'
                    queue.append((next_row, next_col, next_step))
        
        return -1