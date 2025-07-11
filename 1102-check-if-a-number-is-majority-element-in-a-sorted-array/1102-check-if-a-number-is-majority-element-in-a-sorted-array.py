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

        # v2: implement lower bound and upper bound function myself
        def lower_bound(nums: List[int], target: int) -> int: # 포함하는 index구하기
            left = 0
            right = len(nums)
            res = 0
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target: # target이 클때만 옮긴다는 같을때는 오른쪽만 이동시키는거야~ right가 움직이니깐 자연스럽게 계속 왼쪽을 체크하겠지
                    left = mid + 1
                else: # 타켓이 작거나 같으면 우리는 계속해서 밑으로 내려가면서 체크해야겠지 mid 포함해서 
                    right = mid
            return left

        def upper_bound(nums: List[int], target: int) -> int: # 초과하는 index구하기
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target: # 타켓하고 같을때마저 left를 옮겨버려 그래서 초과 index가 나오겠지
                    left = mid + 1
                else:
                    right = mid

            return left
        
        lower_index = lower_bound(nums, target)
        upper_index = upper_bound(nums, target)

        return len(nums) / 2 < upper_index - lower_index




        # v1 : I remember the binary search module, so it is easy
        # what if I cannot use the module?
        # count =  bisect_right(nums, target) - bisect_left(nums, target)
        # return len(nums) / 2 < count