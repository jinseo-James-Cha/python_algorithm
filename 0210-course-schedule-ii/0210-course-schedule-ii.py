from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort - Kahn's algorithm
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            # b -> a
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for label in range(numCourses):
            if indegree[label] == 0:
                queue.append(label)

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []
        