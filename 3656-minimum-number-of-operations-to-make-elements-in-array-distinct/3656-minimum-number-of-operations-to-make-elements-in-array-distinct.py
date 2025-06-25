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
