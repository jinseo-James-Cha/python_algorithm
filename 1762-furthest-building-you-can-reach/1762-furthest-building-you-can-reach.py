import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # start 0
        # move to next building by using brick or ladder

        # if building 0 height > = building 1 height -> no need brick or ladder
        # if building 0 height < building 1 height -> one ladders or building 1 height - building 0 height
        
        # min heap - greedy
        # min diff -> using brick / big diff -> using ladder
        n = len(heights)
        ladder_allocations = []
        for i in range(n - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            
            heapq.heappush(ladder_allocations, diff)

            if len(ladder_allocations) <= ladders:
                continue
            
            bricks -= heapq.heappop(ladder_allocations)
            if bricks < 0:
                return i
        
        return n - 1

            

        


        # dp?! -> MLE
        # choose ladder or bricks
        # len = 7
        # i = 0 ~ 6
        @cache
        def dp(i, bricks, ladders):
            if i == len(heights)-1:
                return i
            
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                return dp(i+1, bricks, ladders)

            res = i
            if bricks >= diff:
                res = max(res, dp(i+1, bricks - diff, ladders))

            if ladders > 0:
                res = max(res, dp(i+1, bricks, ladders - 1))
            
            return res
        return dp(0, bricks, ladders)
