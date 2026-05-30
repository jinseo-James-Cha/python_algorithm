"""
Description: Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order. 
The same number may be chosen from candidates an unlimited number of times.  

Example:  

Input: candidates = [2,3,6,7],   target = 7

Output: [[2,2,3],[7]]
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return a list of all unique combination?! -> backtrack
        def backtrack(start, curr, remainder):
            if 0 > remainder:
                return
            
            if remainder == 0:
                res.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, remainder - candidates[i])
                curr.pop()
            
        res = []
        backtrack(0, [], target)
        return res
