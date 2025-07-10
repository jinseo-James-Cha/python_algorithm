class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        res = []
        self.backtrack(nums, [], set(), res)
        return res

    def backtrack(self, nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
        # base case / termination condition
        if len(candidate) == len(nums):
            # process solution
            res.append(candidate[:])
            return

        for num in nums: 
            if num not in used:
                # make a decision
                # add num
                candidate.append(num) 
                used.add(num)

                # move further 
                self.backtrack(nums, candidate, used, res)

                # undo decition 
                # backtrack
                candidate.pop()
                used.remove(num)

    