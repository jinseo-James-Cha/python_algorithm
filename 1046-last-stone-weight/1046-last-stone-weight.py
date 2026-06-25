import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        i stone
        choose the heaviest two stones and smash
        and x <= y
        
        1. x == y => both removed
        2. x != y => x removed and y = y - x
        """
        # max heap
        if len(stones) == 1:
            return 1
        
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        # take out two max and loop
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            
            new_weight = y - x
            if new_weight > 0:
                heapq.heappush(max_heap, -new_weight)
        
        return -max_heap[0] if max_heap else 0
