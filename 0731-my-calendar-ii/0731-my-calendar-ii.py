class MyCalendarTwo:
    # sweep line

    def __init__(self):
        self.timeline = {}

    def book(self, startTime: int, endTime: int) -> bool:
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1

        self.timeline.sort()

        curr = 0
        for time in self.timeline:
            curr += self.timeline[time]
            if curr >= 3:
                self.timeline[start] -= 1
                self.timeline[end] += 1
                return False

        return True




    # O(N^2)
    def __init__(self):
        self.bookings = []
        self.double_bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for ds, de in self.double_bookings:
            if ds < endTime and startTime < de:
                return False
            
        for s, e in self.bookings:
            if s < endTime and startTime < e:
                self.double_bookings.append((max(s, startTime), min(e, endTime)))

        self.bookings.append((startTime, endTime))
        return True

        
    # O(N^2)
    # TLE
    # def __init__(self):
    #     self.bookings = {}

    # def book(self, startTime: int, endTime: int) -> bool:
    #     # check
    #     is_valid = True
    #     for curr in range(startTime, endTime):
    #         if curr not in self.bookings:
    #             continue
    #         elif self.bookings[curr] >= 2:
    #             is_valid = False
        
    #     if not is_valid:
    #         return False
        
    #     for curr in range(startTime, endTime):
    #         self.bookings[curr] = self.bookings.get(curr, 0) + 1
    #     return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)