from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list) # adjacent list
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # start? -> no prerequisites -> indegree 0
        stack = deque()
        for course, cnt in enumerate(indegree):
            if cnt == 0:
                stack.append(course)
        

        course_order = []
        while stack:
            curr_course = stack.popleft()
            course_order.append(curr_course)

            for next_course in graph[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    stack.append(next_course)
        
        if len(course_order) == numCourses:
            return course_order
        return []

