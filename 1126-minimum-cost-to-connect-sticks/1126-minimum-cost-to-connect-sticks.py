import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # minimum cost

        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            first_min = heapq.heappop(sticks)
            second_min = heapq.heappop(sticks)
            
            curr_len = first_min + second_min
            res += curr_len
            heapq.heappush(sticks, curr_len)
        
        return res

