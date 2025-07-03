# I need a data structure to add an element in between and get by -3 easily
# largest -> need sort -> sort()? or heapq ?
# save till kth 
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = nums
        heapq.heapify(self.scores)

        # pop till len equals to k
        # so we keep only kth values
        for i in range(len(self.scores) - self.k):
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        # empty scores -> return the new val
        if len(self.scores) == 0:
            heapq.heappush(self.scores, val)
            return val

        heapq.heappush(self.scores, val)
        if len(self.scores) > self.k:
            heapq.heappop(self.scores)
        return self.scores[0]
        # # compare with kth value
        # kthValue = self.scores[0]
            
        # # ignore if new val is less than kth value
        # if kthValue > val:
        #     return kthValue
        # # only if its full, remove kth value and add new val
        # if len(self.scores) == self.k:
        #     heapq.heappop(self.scores)
        # heapq.heappush(self.scores, val)
        
        # return self.scores[0]
        
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)