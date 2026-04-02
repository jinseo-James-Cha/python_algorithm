import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        get minimum rooms
        -> how many meetings are overlapping?
        -> should I consider an overlapping when end time and start time are the same?
        
        need to handle by start time order

        0 5 10 15 20 25 30
        - - -  -  -  -  -
          - -
               -  -
        total 2 meetings

        0 1 2 3 4 5 6 7 8 9 10
            - - -
                      - - - -

        [30]
        30 > 5
        compare prev.end to curr.start
        if prev.end > curr.start -> overlapping
        if prev.end <= curr.start -> no overlapping
        """
        # pirority queue
        intervals.sort(key=lambda x:x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, intervals[i][1])
        return len(free_rooms)


        # sweep line
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        overlaps = 0
        curr_meeting_room = 0
        for time, usage in events:
            curr_meeting_room += usage
            overlaps = max(overlaps, curr_meeting_room)
        return overlaps
