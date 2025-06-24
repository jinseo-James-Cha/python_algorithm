import heapq
class MedianFinder:

    def __init__(self):
        self.left_half = [] # max-heap
        self.right_half = [] # min-heap
        
    def addNum(self, num: int) -> None:
        # if num is less than or equal to the max of left half
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)

            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        
        # if num is on right_half
        else:
            heapq.heappush(self.right_half, num)

            if len(self.left_half) < len(self.right_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def findMedian(self) -> float:
        # heap[0]은 가장 작은 값을 단순히 조회(read-only) 할 때 사용합니다.

        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        return -self.left_half[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()