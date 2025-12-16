from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # directed acyclic graph -> kahn's algorithm with topological sort
        # visit node that having no directed edge and visit its neighbor and minus 1
        # if it is indegree 0, then insert into the queue

        hashmap = defaultdict(list)
        indegree = defaultdict(int)
        for dest, src in prerequisites:
            hashmap[src].append(dest)
            indegree[dest] += 1
        
        # initialize with root node
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # loop
        tookCourses = []
        while queue:
            currCourse = queue.popleft()
            tookCourses.append(currCourse)

            for neighbor in hashmap[currCourse]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return tookCourses if len(tookCourses) == numCourses else []