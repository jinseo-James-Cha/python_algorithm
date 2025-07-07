class TwoSum:

    def __init__(self):
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.arr.sort()

    def find(self, value: int) -> bool:
        left = 0
        right = len(self.arr) - 1

        while left < right:
            if value > self.arr[left] + self.arr[right]:
                left += 1
            elif value < self.arr[left] + self.arr[right]:
                right -= 1
            else:
                return True
        return False

# add 1 3 5
# find 4 -> 1, 3 -> True
# find 7 -> no two numbers -> False

# I need ascending order number to use two pointers or Binary search
# but how to increase size of array easily and put in the middle of the size?
# append and sort?

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)