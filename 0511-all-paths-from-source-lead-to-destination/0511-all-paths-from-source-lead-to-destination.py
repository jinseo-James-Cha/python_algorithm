class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2  # visiting(1) → cycle 감지 False 

            # destination이 아닌데 outgoing이 없으면 dead-end -> 실패
            if not adjacent_list[node] and node != destination:
                return False

            # destination인데 outgoing edge가 있다면 실패
            if node == destination and adjacent_list[node]:
                return False

            state[node] = 1
            for neighbor in adjacent_list[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2
            return True

        state = [0] * n  # 0: unvisited, 1: visiting, 2: safe(검증 완료)
        adjacent_list = defaultdict(list)
        for a, b in edges:
            adjacent_list[a].append(b)
        
        return dfs(source)