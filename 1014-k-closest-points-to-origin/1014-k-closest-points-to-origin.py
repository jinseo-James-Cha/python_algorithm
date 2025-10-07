import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # as k much, we need the answers
        # priority queue -> max heap
        
        max_heap = []
        for x, y in points:
            val = (x-0)**2 + (y-0)**2
            heapq.heappush(max_heap, [-val, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        for val, x, y in max_heap:
            res.append([x, y])
        
        return res
