from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # adjacent list
        def dfs(city):
            visited_cities[city] = True

            for next_city in adjacent_list[city]:
                if visited_cities[next_city] == False:
                    dfs(next_city)


        n = len(isConnected)
        res = 0
        visited_cities = [False] * n
        adjacent_list = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adjacent_list[i].append(j)
            
        for city in range(n):
            if visited_cities[city] == False:
                res += 1
                dfs(city)
        return res


        # # DFS X
        # def is_within_bound(row, col):
        #     return 0 <= row < len(isConnected) and 0 <= col < len(isConnected[0])
        
        # def dfs(i, j):
        #     visited[i][j] = True
            
        #     for r, c in DIR:
        #         next_r, next_c = r + i, c + j
        #         if is_within_bound(next_r, next_c) and visited[next_r][next_c] == False and isConnected[next_r][next_c] == 1:
        #             dfs(next_r, next_c)
            
        
        # n = len(isConnected)
        # DIR = [(-1,0), (1,0), (0,-1), (0, 1)]
        # visited = [[False] * n for _ in range(n)]
        # res = 0

        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and visited[i][j] == False:
        #             res += 1
        #             dfs(i,j)

        # return res