class MyCalendarTwo:

    def __init__(self):
        self.events = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        copied_events = self.events[:]
        copied_events.append((startTime, 1))
        copied_events.append((endTime, -1))

        copied_events.sort()

        curr_score = 0
        for time, score in copied_events:
            curr_score += score
            if curr_score >= 3:
                return False
        
        self.events = copied_events[:]
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

"""
 10 - 20
             50- 60
 10      40
5 15 X
510
        25     55 
"""