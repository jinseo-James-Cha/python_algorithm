class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals -> sweep line algorithm
        # define events
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        # sort events
        events.sort(key= lambda x: (x[0], x[1]))
        


        max_rooms, curr_rooms = 0, 0
        for k, v in events:
            curr_rooms += v
            max_rooms = max(max_rooms, curr_rooms)
        return max_rooms