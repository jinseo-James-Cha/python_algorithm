import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return 1
        
        # max heap
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        # take out two max and loop
        while len(max_heap) > 1:
            first_max = -heapq.heappop(max_heap)
            second_max = -heapq.heappop(max_heap)
            
            new_weight = first_max - second_max
            if new_weight > 0:
                heapq.heappush(max_heap, -new_weight)
        
        return -max_heap[0] if max_heap else 0
