from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a,b] =>     b -> a

        # topology algorithm
        adj = defaultdict(list)
        indegrees = {}
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegrees[dest] = indegrees.get(dest, 0) + 1
        
        # start with zero indegree
        zero_indegrees = deque()
        for i in range(numCourses):
            if i not in indegrees:
                zero_indegrees.append(i)
        
        answer = []
        while zero_indegrees:
            current = zero_indegrees.popleft()
            answer.append(current)

            for neighbor in adj[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zero_indegrees.append(neighbor)
        
        return answer if len(answer) == numCourses else []