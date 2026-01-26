class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        
        # start from Friday => +4
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        total_days = 0
        
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365
            
        for m in range(month-1):
            total_days += month_days[m]
            if m == 1 and is_leap(year):
                total_days += 1
        
        total_days += day
        
        return days[(total_days + 4) % 7]