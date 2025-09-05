class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1 <= nums.length <= 6 -> backtracking?
        def backtrack(curr, used):
            if len(curr) == len(nums):
                res.append(curr[:])
            
            for num in nums:
                if num not in used:
                    curr.append(num)
                    used.add(num)
                    
                    backtrack(curr, used)
                    
                    curr.pop()
                    used.remove(num)
        
        res = []
        backtrack([], set())
        return res
        

















        res = []
        seen = set()

        def backtrack(current):
            if len(current) == len(nums):
                res.append(current[:])
            
            for num in nums:
                if num not in seen:
                    current.append(num)
                    seen.add(num)
                    backtrack(current)
                    current.pop()
                    seen.remove(num)
        
        backtrack([])
        return res










    #     # backtracking
    #     res = []
    #     self.backtrack(nums, [], set(), res)
    #     return res

    # def backtrack(self, nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
    #     # base case / termination condition
    #     if len(candidate) == len(nums):
    #         # process solution
    #         res.append(candidate[:])
    #         return

    #     for num in nums: 
    #         if num not in used:
    #             # make a decision
    #             # add num
    #             candidate.append(num) 
    #             used.add(num)

    #             # move further 
    #             self.backtrack(nums, candidate, used, res)

    #             # undo decition 
    #             # backtrack
    #             candidate.pop()
    #             used.remove(num)

    