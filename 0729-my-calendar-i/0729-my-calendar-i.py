class MyCalendar:

    def __init__(self):
        self.bookings = []
        
    #         startTime5 ----- endTime 10
    #              3---------------9
    #       1---------5         7----------11
    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if start < endTime and end > startTime:
                return False
        
        self.bookings.append((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)