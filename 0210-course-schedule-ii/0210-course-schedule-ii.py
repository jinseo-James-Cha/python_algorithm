from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] = indegree.get(dest,0) + 1
        
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []
        while zero_indegree_queue:

            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            if vertex in adj:
                for neighbor in adj[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)
        
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []

         