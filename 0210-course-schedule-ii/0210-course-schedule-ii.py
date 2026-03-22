from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        b take first and then can a

        [1,0],[2,0],[3,1],[3,2]]

        0 -> 1, 2
        1 -> 3
        2 -> 3
        3
        
        0, 1, 2, 3
        or 0, 2, 1, 3

        directed acyclic graph
        -> kahn's algorithm with topological sort
        tracking indegree and 0 and then can take the course
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # initiate with indegree 0
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        res = []
        while queue:
            curr_course = queue.popleft()
            res.append(curr_course)

            for next_course in graph[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []