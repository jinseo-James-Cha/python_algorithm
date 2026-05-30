"""

Description: Given an array nums of distinct integers, 
return all the possible permutations. You can return the answer in any order.

Example:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

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