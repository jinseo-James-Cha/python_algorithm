class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # heapq
        res = 0
        ladder_allocations = []
        for h1, h2 in zip(heights[:len(heights)], heights[1:]):
            diff = h2 - h1
            if diff <= 0:
                res += 1
                continue

            heapq.heappush(ladder_allocations, diff)

            if len(ladder_allocations) > ladders:
                bricks -= heapq.heappop(ladder_allocations)
            
            if bricks < 0:
                break
            
            res += 1
        return res
            
