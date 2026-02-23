class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #  0 5 10 15 20 25 30
        #A - -  -  -  -  -  -
        #B   -  -
        #C         - -

        # check intervals by start order
        
        # case 1: non-overlapping
        # if prev.end < curr.start
        #   update prev = curr

        # case 2: overlapping
        # if prev.end >= curr.start
        #   append curr

        # every time get lengh of the queue
        intervals.sort(key=lambda x:x[0])

        pq = [intervals[0][1]] # 30 -> 10,30
        max_len = 1

        for curr_start, curr_end in intervals[1:]:
            minimum_end = pq[0]

            if minimum_end <= curr_start:
                heapq.heappop(pq)
                
            heapq.heappush(pq, curr_end)
            max_len = max(max_len, len(pq))

        return max_len

        # priority queue
        # 0 ------- 30 start 31 ..
        # 
        # 30
        intervals.sort()

        rooms = []
        heapq.heappush(rooms, intervals[0][1]) # add first's end time
        
        for start, end in intervals[1:]:
            if start >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)
        return len(rooms)

        # sweep line
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()

        res = 0
        curr_room = 0
        for point, score in events:
            curr_room += score
            res = max(res, curr_room)
        
        return res




        # intervals.sort()
        # res = 1
        # curr_room = 1
        # prev_end = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] < prev_end:
        #         curr_room += 1
        #         res = max(res, curr_room)
                
        #     else:
        #         curr_room -= 1
        #     prev_end = min(prev_end, intervals[i][1])
        # return res
