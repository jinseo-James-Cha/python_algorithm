# time O(n)
# space O(n)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = [False] * 128 # no meaning with 128, just 2**7 and enough space

        # reverse the array
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0


# brute force O(n^2)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # ensure all in array is distinct
        # operate - remove 3 elements from the beginning
        # [1,2,3,4,2,3,3,5,7]
        # [4,2,3,3,5,7]
        # [3,5,7]
        # len(set) == len(array) -> return?
        count = 0
        for i in range(0, len(nums),3):
            arr = nums[i:]
            s = set(arr)
            if len(s) == len(arr):
                return count
            count += 1
        return count
