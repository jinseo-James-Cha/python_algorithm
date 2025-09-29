from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # 1 ~ n
        # [prevCourse, nextCourse] => prev -> next

        # if cyclic graph -> return -1
        
        # kahn's algorithm
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)
        for prevCourse, nextCourse in relations:
            adj_list[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        
        # initial course with indegree 0
        pq = deque()
        for i in range(1, n+1):
            if in_degree[i] == 0:
                pq.append((i, 1))
        
        # if cyclic
        if not pq:
            return -1
        
        taken_courses = []
        min_semester = 1
        while pq:
            curr_course, semester = pq.popleft()
            taken_courses.append(curr_course)
            min_semester = semester

            for neighbor in adj_list[curr_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    pq.append((neighbor, semester + 1))
        
        return -1 if n != len(taken_courses) else min_semester



        

        

