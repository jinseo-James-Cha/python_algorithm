from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # 1. define hashmap with list
        # 1-1 count indegree of dest

        # 2. find and insert root node which has 0 indegree into double ended queue
        
        # 3. loop the queue
        # 3-1 popleft the first one which is 0 indegree dest node
        # 3-2 tookCourses += 1
        # 3-3 loop hashmap[poppedNode]'s neighbors and minus its indegree
        # 3-4 if indegree ==0 then insert into the queue

        # 4. check tookCourses == numCourses
        
        # 1
        hashmap = defaultdict(list)
        indegree = defaultdict(int)
        for dest, src in prerequisites:
            hashmap[src].append(dest)
            indegree[dest] += 1
        
        # 2
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        # 3
        tookCourse = 0
        while queue:
            currCourse = queue.popleft()
            tookCourse += 1

            for neighbor in hashmap[currCourse]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return tookCourse == numCourses