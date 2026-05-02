class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, index):
            res.append(curr[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        nums.sort()
        res = []
        backtrack([], 0)
        return res