from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort - kahn's algorithm
        
        # 1. graph and indegree
        graph = defaultdict(list)
        indegree = [0] * numCourses # 0~numCourses-1
        # b -> a
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # 2. add initial if indegree == 0
        queue = deque()
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if numCourses == len(res) else []
