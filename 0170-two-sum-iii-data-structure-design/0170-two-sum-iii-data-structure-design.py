class TwoSum:
    # v2 : hash map
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for k in self.nums.keys():
            x = value - k
            # not the same number
            # like 14 and 7 and 7 
            if k != x:
                if x in self.nums:
                    return True
            elif self.nums[k] > 1:
                return True
        return False

    # v1 : sorted list
    # def __init__(self):
    #     self.arr = []
    #     self.isSorted = False

    # def add(self, number: int) -> None:
    #     self.arr.append(number)
    #     self.isSorted = False

    # def find(self, value: int) -> bool:
    #     if not self.isSorted:
    #         self.arr.sort()
    #         self.isSorted = True

    #     left = 0
    #     right = len(self.arr) - 1

    #     while left < right:
    #         if value > self.arr[left] + self.arr[right]:
    #             left += 1
    #         elif value < self.arr[left] + self.arr[right]:
    #             right -= 1
    #         else:
    #             return True
    #     return False

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