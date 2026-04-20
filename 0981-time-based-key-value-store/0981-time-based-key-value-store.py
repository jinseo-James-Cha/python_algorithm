"""
time based key-value

key : multiple values

what we search key and timebased

key: (time, val)

{foo: (1, bar), (4, bar2) }
set - foo bar 1
get - foo 1 -> bar
get - foo 3 -> bar
set - foo bar2 4
get - foo 4 -> bar2
get - foo 5 -> bar2
"""

from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        if timestamp < self.time_map[key][0][0]:
            return ""

        left = 0
        right = len(self.time_map[key])
        while left < right:
            mid = (left + right) // 2
            if self.time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.time_map[key][left-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)