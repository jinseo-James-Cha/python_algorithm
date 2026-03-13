import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sweep line
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort()

        max_room = 0
        total_score = 0
        for position, score in events:
            total_score += score
            max_room = max(max_room, total_score)
        return max_room


        """
        add close position in heap
        and check if heap[0] > start -> add end in the heap and renew max room
        """
        minimum_room = 1
        
        intervals.sort()
        
        pq = []
        heapq.heappush(pq, intervals[0][1])

        for i in range(1, len(intervals)):
            curr = intervals[i]
            while pq and curr[0] >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, curr[1])
            minimum_room = max(minimum_room, len(pq))

        return minimum_room
        