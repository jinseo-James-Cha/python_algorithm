from bisect import bisect_left, bisect_right

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # 1. problem
        # nums -> ascending order
        # True -> target == "majority element"
        # majority element == appears more than nums.length / 2 times
        # [2,4,5,5,5,5,5,6,6] , target 5
        # len 9 / 2 -> 4.5 < 5
        # (len / 2 ) < nums of target

        # 2. intuition
        # loop to get count for  nums of target in nums
        # we can use Binary Search to get upper-bound - lower bound == count of the target num
        # and return len(nums) / 2 < count

        # 3. complexity
        # O(log n) -> 1000

        # 4. data structure
        # int count, mid, left, right

        # count = 0
        # left = 0
        # right = len(nums) # to get bound using len instead of len - 1 
        # while left < right: # using < for bound question instead of left <= right
        #     # how to get index of lower and upper bound? 
        #     # let me use a module

        count =  bisect_right(nums, target) - bisect_left(nums, target)
        return len(nums) / 2 < count