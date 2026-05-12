from collections import deque
class PhoneDirectory:

    def __init__(self, maxNumbers: int):        
        self.queue = deque(range(maxNumbers))
        self.is_slot_available = [True] * maxNumbers
        

    def get(self) -> int:
        if not self.queue:
            return -1
        
        curr_used = self.queue.popleft()
        self.is_slot_available[curr_used] = False
        return curr_used

    def check(self, number: int) -> bool:
        return self.is_slot_available[number]
        

    def release(self, number: int) -> None:
        if self.is_slot_available[number]:
            return

        self.queue.append(number)
        self.is_slot_available[number] = True
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)