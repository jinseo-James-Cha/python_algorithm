import heapq
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dijkstra
        # starting 0 -> end n
        dist = [float('inf')] * (n+1)
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)

            if curr_dist > dist[curr_node]:
                continue

            for step in [1, 2, 3]:
                next_node = curr_node + step
                if next_node-1 < n:
                    next_dist = curr_dist + costs[next_node-1] + step**2

                    if dist[next_node] > next_dist:
                        dist[next_node] = next_dist
                        heapq.heappush(pq, (next_dist, next_node))
        return dist[n]





        def dp(i):
            if i == 0:
                return 0
            
            if i not in memo:
                res = float('inf')
                if i >= 1:
                    res = min(res, dp(i-1) + 1**2)
                if i >= 2:
                    res = min(res, dp(i-2) + 2**2)
                if i >= 3:
                    res = min(res, dp(i-3) + 3**2)

                memo[i] = res + costs[i-1]
            return memo[i]
        memo = {}
        return dp(n)