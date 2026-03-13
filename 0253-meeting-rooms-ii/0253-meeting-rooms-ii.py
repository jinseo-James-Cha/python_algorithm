import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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
            # if pq[0] > curr[0]:
            #     heapq.heappush(pq, curr[1])
            #     minimum_room = max(minimum_room, len(pq))
            # else:
            while pq and curr[0] >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, curr[1])
            minimum_room = max(minimum_room, len(pq))

        return minimum_room
        