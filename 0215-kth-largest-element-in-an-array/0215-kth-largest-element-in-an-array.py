import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        kth largest -> max heap and take out 0?

        1 2 3 4 5
        1 2 3
          2 3 4
            3 4 5 
            pop()
        3 7 8 1 2
        3 7 8
          3 7 8
        """
        pq = [] # min-heap
        for num in nums:
            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)

            # if len(pq) < k:
            #     heapq.heappush(pq, num)
            # elif pq[0] < num:
            #     heapq.heappop(pq)
            #     heapq.heappush(pq, num)
        return pq[0]
        # [3,2,1,5,6,4]

