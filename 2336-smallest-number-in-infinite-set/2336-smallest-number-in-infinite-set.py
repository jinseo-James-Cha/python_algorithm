import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = []
        self.in_heap = set()
        self.curr_num = 1

    def popSmallest(self) -> int:
        if self.min_heap and self.min_heap[0] < self.curr_num:
            self.in_heap.remove(self.min_heap[0])
            return heapq.heappop(self.min_heap)

        curr = self.curr_num
        self.curr_num += 1
        return curr

    def addBack(self, num: int) -> None:
        if num < self.curr_num:
            if num not in self.in_heap:
                self.in_heap.add(num)
                heapq.heappush(self.min_heap, num)
        
"""
["popSmallest", curr_num =2
"addBack", 1 min_heap = [1]
"addBack", 1 min_heap = [1]
"popSmallest", 1 min_heap[]
"addBack", 1 min_heap[1]
"popSmallest", 1 min_heap[]
"popSmallest", 2 curr_num = 3
"popSmallest"] 3 curr_num =

"""

"""
["SmallestInfiniteSet",
"popSmallest", -> 1 curr_num 2
"addBack", 1 -> min_heap[1]
"popSmallest", 1 -> min_heap[]
"popSmallest", 2 -> curr_num 3
"popSmallest", 3 -> curr_num 4
"addBack", 2 -> min_heap[2]
"addBack", 3 -> min_heap[2, 3]
"popSmallest", 2
"popSmallest"] 3

"""


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)