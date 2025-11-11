class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, visited):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in visited:
                    curr.append(num)
                    visited.add(num)

                    backtrack(curr, visited)

                    curr.pop()
                    visited.remove(num)

        res = []
        backtrack([], set())
        return res