from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular 0
        # square 1

        # stand in queue
        # sandwitches in stack
        student_queue = deque(students)
        sandwiches.reverse()
        
        while student_queue:
            # find my preference
            n = len(student_queue)
            for _ in range(n):
                if student_queue[0] == sandwiches[-1]:
                    student_queue.popleft()
                    sandwiches.pop()
                else:
                    student_queue.append(student_queue.popleft())
            
            if n == len(student_queue):
                return n
        return 0
        