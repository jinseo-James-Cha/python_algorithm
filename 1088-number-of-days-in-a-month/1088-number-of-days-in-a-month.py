class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[M-1] + (M == 2 and (Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0))