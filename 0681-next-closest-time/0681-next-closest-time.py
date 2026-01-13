class Solution:
    def nextClosestTime(self, time: str) -> str:
        get_numbers = [] # 1, 9, 3, 4
        for t in time:
            if t.isnumeric():
                get_numbers.append(int(t))
        base_time_in_minute = (get_numbers[0]*10 + get_numbers[1]) * 60 + (get_numbers[2]*10+ get_numbers[3])
        
        def backtrack(start, curr):
            nonlocal base_time_in_minute, next_closest_time_difference, next_closest_time
            if len(curr) == 4:
                hour = curr[0]*10 + curr[1]
                minute = curr[2]*10 + curr[3]
                if hour <= 23 and minute <= 59: # valid time
                    curr_time_in_minute = hour * 60 + minute
                    
                    if curr_time_in_minute - base_time_in_minute > 0:
                        if next_closest_time_difference > curr_time_in_minute - base_time_in_minute:
                            next_closest_time_difference = curr_time_in_minute - base_time_in_minute
                            next_closest_time = curr_time_in_minute
                    elif curr_time_in_minute - base_time_in_minute < 0: # next day
                        gap = (24 * 60 - base_time_in_minute) + curr_time_in_minute
                        if next_closest_time_difference > gap:
                            next_closest_time_difference = gap
                            next_closest_time = curr_time_in_minute
                return
            
            for i in range(4): # 4 digits
                curr.append(get_numbers[i])
                backtrack(i, curr)
                curr.pop()
        
        next_closest_time_difference = float('inf')
        next_closest_time = base_time_in_minute
        backtrack(0, [])
        
        # return the format
        h = next_closest_time // 60
        m = next_closest_time % 60
        
        h_s = str(h) if h >= 10 else "0"+str(h)
        m_s = str(m) if m >= 10 else "0"+str(m)
        return h_s + ":" + m_s