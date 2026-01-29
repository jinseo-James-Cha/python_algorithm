import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # minimum number of conference room ..
        # -> how many meetings are intersection
        # -> sweep line algorithm


        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()

        max_room_used = 0
        curr_room = 0
        for time, score in events:
            curr_room += score
            max_room_used = max(max_room_used, curr_room)
        return max_room_used

















        # priority queue
        intervals.sort(key=lambda x: x[0])

        rooms = []
        heapq.heappush(rooms, intervals[0][1]) # add first's end time
        
        for start, end in intervals[1:]:
            if start >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)
        return len(rooms)
        
        
        
        
        
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