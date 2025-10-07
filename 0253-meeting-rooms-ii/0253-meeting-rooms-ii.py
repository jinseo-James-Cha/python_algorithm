class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals -> sweep line algorithm
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        
        max_rooms, curr = 0, 0
        for k, v in events:
            curr += v
            max_rooms = max(max_rooms, curr)
        return max_rooms