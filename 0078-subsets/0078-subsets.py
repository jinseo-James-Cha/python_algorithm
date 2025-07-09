class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, [], nums, res)
        return res
    
    def backtrack(self, i: int, curr_subset: List[int], nums: List[int], res: List[List[int]]) -> None:
        # base case: if all elements have been considered, add the current subset to the output
        if i == len(nums):
            res.append(curr_subset[:])
            return

        # include the current element 
        # and recursively explore all paths that branch from this subset
        curr_subset.append(nums[i])
        self.backtrack(i + 1, curr_subset, nums, res)

        # exclude the current element
        # and recursively explore all paths that branch from this subset
        curr_subset.pop()
        self.backtrack(i + 1, curr_subset, nums, res)

