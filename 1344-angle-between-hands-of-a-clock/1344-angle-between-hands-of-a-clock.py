class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        hour and minutes .. they make 2 angles and return a smaller one.

        #hour angle
        12 hour = 360 degree
        1 hour = 30 degree
        5 hour = 150 degree
        => hour % 12 *  30 degree
        => However, Hour angle has additional movement by minute
        => (hour % 12 + minutes/60) * 30 degree

        #minute angle
        60 min = 360 degree
        1 min = 6 degree
        5 min = 6 * 5 = 30 degree

        calculate each angel and remove common angle => the actual angle between two angles
        return min angel either inner or outer 
        """
        one_hour_angle = 360 // 12
        one_min_angle = 360 // 60
        
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        minute_angle = minutes * one_min_angle

        removed_common_angle = abs(hour_angle - minute_angle)
        return min(removed_common_angle, 360 - removed_common_angle)
