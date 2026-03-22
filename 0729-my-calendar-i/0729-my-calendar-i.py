from bisect import bisect_left
class MyCalendar:
    def __init__(self):
        self.bookings = []
        
    # O(N log N)
    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.bookings, (startTime, endTime))

        if i > 0 and self.bookings[i - 1][1] > startTime:
            return False

        if i < len(self.bookings) and self.bookings[i][0] < endTime:
            return False
        
        self.bookings.insert(i, (startTime, endTime))
        return True


    # O(N^2)
    # def book(self, startTime: int, endTime: int) -> bool:
    #     for s, e in self.bookings:
    #         if not (endTime <= s or startTime >= e):
    #             return False
    #     self.bookings.append((startTime, endTime))
    #     return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)