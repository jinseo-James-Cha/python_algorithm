from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # n cities -> roads connecting cities
        # roads ==> edges and bidirectional
        # a <-> b

        # network rank of two cities ==> total number of directly connected roads to either city
        # if load is directly both -> count 1

        # return maximal network rank

        # 0: 1, 3
        # 1: 0, 2, 3
        # 2: 1
        # 3: 0, 1

        """
        0 - 1 rank = 0 roads + 1 roads and 0, 1 connects -1 => 5 - 1 = 4

        1 - 2 rank = 3 roads + 1 loads and 1,2 connects -1 => 4 - 1 = 3

        2 - 3 rank = 1 roads + 2 loads and not connected = > 3


        0: 1, 3
        1: 0, 2, 3
        2: 1, 3, 4
        3: 0, 1, 2
        4: 2

        0-1 -> 2+ 3 - 1 = 4
        1-2 -> 3+3 - 1 = 5
        2-3 -> 3+3 - 1 = 5
        3-4 -> 3+1 = 4


        0: 1
        1: 0, 2
        2: 1, 3, 4
        3: 2
        4: 2
        5: 6, 7
        6: 5
        7: 5

        2-5 : 3 + 2 => 5
        """

        adj_list = [[] for _ in range(n)]
        adj = defaultdict(set)
        for a, b in roads:
            adj_list[a].append(b)
            adj_list[b].append(a)

            adj[a].add(b)
            adj[b].add(a)
        
        # greedy
        max_network_rank = 0
        for i in range(n-1):
            for j in range(i+1, n):
                total = len(adj_list[i] + adj_list[j])
                total -= 1 if i in adj[j] else 0
                max_network_rank = max(max_network_rank, total)
        return max_network_rank

        