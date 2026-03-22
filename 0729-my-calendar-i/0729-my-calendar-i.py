class MyCalendar:
    """
    10 15 20 25 30
    -  -  -
       -  -  -
          -  -  -
             -  -
    (10, 20) (15 25) x, (5 15) x
    (20, 2)

    """

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.bookings:
            if s < endTime and startTime < e:
                return False
        self.bookings.append((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)