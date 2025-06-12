# v2: sliding window
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.window_sum = 0
        self.window_size = 0
        self.size = size

    def next(self, val: int) -> float:
        poped = 0
        if len(self.window) >= self.size:
            poped = self.window.popleft()

        self.window.append(val)
        self.window_sum += val - poped
        return self.window_sum / len(self.window)


# just for anwer submit.. lets try another version with sliding window
# class MovingAverage:

#     def __init__(self, size: int):
#         self.arr = []
#         self.size = size

#     def next(self, val: int) -> float:
#         if len(self.arr) >= self.size:
#             self.arr = self.arr[1:]
#         self.arr.append(val)
#         return sum(self.arr) / len(self.arr)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)