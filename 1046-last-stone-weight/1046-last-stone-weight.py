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
        # bucket sort or counting sort
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        for weight in stones:
            buckets[weight] += 1

        biggest_weight = 0 
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight


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
